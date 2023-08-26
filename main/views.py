from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import  authenticate #add this
from django.contrib.auth import login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime
from .models import SocietyList,MembersList
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .forms import ChargesForm,MembersForm,EditSocietyForm,EditMembersForm
import json,os
import pandas as pd
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request,'index.html')

def logout_user(request):
    logout(request)
    return redirect('login')

# @login_required
def homeAfterLogin(request):
    print(request.user)
    return render(request,'homeAfterLogin.html')

def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                print(request, f"You are now logged in as {username}.")
                query_results = SocietyList.objects.filter(user=user)   
                return render(request, "society_detail.html",{'query_results':query_results})
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"login_form":form})



# @login_required
def addSociety(request):
    user = request.user
    if request.method == "POST":
        societyName = request.POST.get('societyName')
        societyNameExists = SocietyList.objects.filter(user= user, societyName=societyName)
        print(societyNameExists)
        if societyNameExists:
            return HttpResponseRedirect(request.path_info)
        regno = request.POST.get('regno')
        address = request.POST.get('address')
        user = user
        request.session['societyName'] = societyName
        request.session['regno'] = regno
        request.session['address'] = address
        context={'societyName':societyName
                 ,'regno':regno
                 ,'address':address
                 } 

        return render(request, 'selectChargesFields.html',context)       
    query_results = SocietyList.objects.filter(user=user)
    return render(request, 'addSociety.html',{'query_results':query_results})

# @login_required
def societyMembers(request, item_name):
    user = request.user
    memberSocietyName = item_name
    context={}
    context['form']= MembersForm()
    form = MembersForm(request.POST)
    members_dict = {}
    item = get_object_or_404(SocietyList,user=user, societyName=item_name)
    members_dict['memberSocietyName']=item
    if request.method == "POST":
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                if value!='':
                    members_dict[key]=value
        members_dict['date_add_member'] = datetime.today()
        members_dict['user'] = user
        memberNameExists = MembersList.objects.filter(
            user= user, 
            memberSocietyName=  item,
            Member_Name=members_dict['Member_Name'])
        if memberNameExists:
            return redirect('society'+ item_name +'societyMembers')
        new_member = MembersList(**members_dict)
        new_member.save() 
        return redirect('/society/'+ item_name +'/societyMembers')
    query_results = MembersList.objects.filter(user=user,memberSocietyName=item)
    charges_fields = SocietyList.objects.get(user=user,societyName=item)
    society_charges=charges_fields.charges_fields
    society_charges = json.loads(society_charges.replace('\'','"'))
    display_charges=['Member_Name','Flat_No','Opening_Balance','Closing_Balance']
    for k,v in society_charges.items():
        if v !='':
            display_charges.append(k)
    context['display_charges'] = display_charges
    form = MembersForm(society_charges)

    context = {
        'item': item,
        'query_results': query_results,
        'form': form,
        'display_charges' : display_charges
     }
    return render(request, 'societyMembers.html', context)

def selectChargesFields(request):
    user = request.user
    if request.method == "POST":
        print('inside selectChargesFields')
        context={}
        context['form']= ChargesForm()
        Electricity_Charges = request.POST.get('Electricity_Charges')
        Water_Charges = request.POST.get('Water_Charges')    
        Service_Charges = request.POST.get('Service_Charges')    
        Municipal_Tax = request.POST.get('Municipal_Tax')    
        Sinking_Fund = request.POST.get('Sinking_Fund')    
        Repair_Fund = request.POST.get('Repair_Fund')    
        Maintainance_Charges = request.POST.get('Maintainance_Charges')
        societyName = request.session['societyName'] 
        regno = request.session['regno'] 
        address = request.session['address'] 
        selected_fields = [Electricity_Charges,Water_Charges,Service_Charges,Municipal_Tax,
                           Sinking_Fund,Repair_Fund,Maintainance_Charges]
        selected_fields = [x for x in selected_fields if x!=None]  
        context['selected_fields']=selected_fields  
        context['societyName']  = societyName    
        new_society = SocietyList(
                    societyName=societyName, 
                    regno=regno, 
                    address=address, 
                    date_add_society=datetime.today(),
                    user = user,
                    charges_fields= json.dumps(selected_fields)
            )
        new_society.save()     
        return render(request,'addChargesFields.html',context)        
    return render(request,'selectChargesFields.html')

def addDefaultCharges(request):
    if request.method == 'POST': 
            form = ChargesForm(request.POST)
            if form.is_valid():
                charges_dict = {}
                for key, value in form.cleaned_data.items():
                    charges_dict[key]=value
                societyName = request.session['societyName'] 
                query_res = SocietyList.objects.get(user = request.user , societyName=societyName) 
                query_res.charges_fields = charges_dict
                query_res.save()
                return redirect('/addSociety')
            
def editSociety(request,name):
    
    if request.method == 'POST': 
            form = EditSocietyForm(request.POST)
            if form.is_valid():
                changes_dict = {}
                for key, value in form.cleaned_data.items():
                    changes_dict[key]=value
                societyNameExists = SocietyList.objects.filter(user= request.user, societyName=changes_dict['Society_Name'])
                # print(societyNameExists)
                # if societyNameExists:
                #     return HttpResponseRedirect(request.path_info)
                editSocietyFields = SocietyList.objects.get(user=request.user,societyName=name)
                editSocietyFields.societyName=changes_dict['Society_Name']
                editSocietyFields.regno=changes_dict['Reg_No']
                editSocietyFields.address=changes_dict['Address']
                editSocietyFields.save()                
                return HttpResponseRedirect('/addSociety')
    
    editSocietyFields = SocietyList.objects.get(user=request.user,societyName=name)
    societyDetails ={}
    societyDetails['Society_Name']=editSocietyFields.societyName
    societyDetails['Reg_No']=editSocietyFields.regno
    societyDetails['Address']=editSocietyFields.address
    form = EditSocietyForm(societyDetails)
    context = {'form': form}
    return render(request,'editSociety.html', context)



def deleteMember(request,name, memberName):
    print(memberName)
    MembersList.objects.filter(
        user=request.user,
        memberSocietyName=SocietyList.objects.get(
            user=request.user,
            societyName=name), 
        Member_Name=memberName ).delete()
    return HttpResponseRedirect('/society/' + name)

def editMemberDetails(request,name,memberName):
    item = get_object_or_404(SocietyList,user=request.user, societyName=name) 
    if request.method == 'POST': 
            form = EditMembersForm(request.POST)
            if form.is_valid():
                members_dict = {}
                for key, value in form.cleaned_data.items():
                    members_dict[key]=value
                # memberNameExists = MembersList.objects.filter(
                #     user= request.user, 
                #     memberSocietyName=  item,
                #     Member_Name=members_dict['Member_Name'])
                # if memberNameExists:
                #     return HttpResponseRedirect('societyMembers')
                MembersList.objects.filter(user=request.user,memberSocietyName=item, Member_Name=memberName).update(**members_dict)              
                return HttpResponseRedirect('/society/'+ item.societyName)
    
    # query_results = MembersList.objects.filter(user=request.user,memberSocietyName=item, Member_Name=memberName)  
    society_charges=item.charges_fields
    society_charges = json.loads(society_charges.replace('\'','"'))
    display_charges=['Member_Name','Flat_No','Opening_Balance','Closing_Balance']
    for k,v in society_charges.items():
        if v !='':
            display_charges.append(k)
    context={}
    context['display_charges'] = display_charges
    form = MembersForm(society_charges)

    context = {
        'item': name,
        # 'query_results': query_results,
        'form': form,
        'display_charges' : display_charges
     }
    return render(request,'editSociety.html', context)

def uploadMemberDetails(request,name):
    if request.method == 'POST':
        members_list_df = pd.read_csv(request.FILES['file'],index_col=False)
        # contentOfFile = file1.read()
    print(members_list_df.to_dict())
    print()
    
#---------------------------------------------------------------------------------------------------    





def society_detail(request):
    user = request.user      
    query_results = SocietyList.objects.filter(user=user)
    return render(request, 'society_detail.html',{'query_results':query_results})

def add_new_society(request):
    user = request.user
    if request.method == "POST":
        societyName = request.POST.get('Society_name')
        societyNameExists = SocietyList.objects.filter(user= user, societyName=societyName)
        print(societyNameExists)
        if societyNameExists:
            return HttpResponseRedirect(request.path_info)
        panno = request.POST.get('PAN_Number')
        regno = request.POST.get('Registration_Number')
        gstno = request.POST.get('GST_Number')
        ctsno = request.POST.get('CTS_Number')
        address = request.POST.get('address')
        user = user
        
        new_society = SocietyList(
                    societyName=societyName, 
                    regno=regno, 
                    address=address, 
                    date_add_society=datetime.today(),
                    user = user,
                    panno=panno,
                    gstno=gstno,
                    ctsno=ctsno
                    # charges_fields= json.dumps(selected_fields)
            )
        new_society.save()
        # request.session['Society_name'] = societyName
        # request.session['PAN_Number'] = panno
        # request.session['Registration_Number'] = regno
        # context={'societyName':societyName
        #          ,'regno':regno
        #          ,'address':address
        #          } 

        return render(request,'add_charges.html')      

    return render(request,'add_new_society.html')

def deleteSociety(request,name):
    SocietyList.objects.filter(user=request.user,societyName=name).delete()
    return HttpResponseRedirect('/society_detail')

def upload_doc_temp(request,name):
    request.session['Society_name'] = name
    return HttpResponseRedirect('/upload_doc')

def upload_doc(request):
    path = settings.MEDIA_ROOT + '/' + request.user.username + '/' +  request.session['Society_name']
    if not os.path.exists(path):
            os.makedirs(path)
    fs = FileSystemStorage(path)   
    files = os.listdir(path)
    file_names = {}
    file_addr={}
    for f in files:
        if os.path.splitext(f)[0]=='Pan':
            file_names['pan']= f
            file_addr['pan']= path + '/' + f
        if os.path.splitext(f)[0]=='GST':
            file_names['gst']= f
            file_addr['gst']= path + '/' + f
        if os.path.splitext(f)[0]=='CTS':
            file_names['cts']= f
            file_addr['cts']= path + '/' + f
        if os.path.splitext(f)[0]=='Others':
            file_names['oth']= f
            file_addr['oth']= path + '/' + f
    context={
        'file_addr':file_addr,
        'file_names':file_names
    } 
    if request.method == 'POST':
        if 'pan_card' in request.FILES.keys():
            myfile = request.FILES['pan_card']        
            file_name = "Pan." + myfile.name.split(".")[1]
        elif 'gst' in request.FILES.keys():
            myfile = request.FILES['gst']        
            file_name = "GST." + myfile.name.split(".")[1]
        elif 'cts' in request.FILES.keys():
            myfile = request.FILES['cts']        
            file_name = "CTS." + myfile.name.split(".")[1]
        elif 'others' in request.FILES.keys():
            myfile = request.FILES['others']        
            file_name = "Others." + myfile.name.split(".")[1]
        else:
            return render(request,'upload_docs.html',context)
        filename = fs.save(file_name, myfile)
    return render(request,'upload_docs.html',context)


def add_charges(request):
    return render(request,'add_charges.html')