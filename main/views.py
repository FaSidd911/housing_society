from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import  authenticate #add this
from django.contrib.auth import login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime
from .models import SocietyList,MembersList,DefaultChargesList
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
        soc_details = {}
        societyName= request.POST.get('Society_name')
        soc_details['societyName'] = societyName
        societyNameExists = SocietyList.objects.filter(user= user, societyName=societyName)
        print(societyNameExists)
        if societyNameExists:
            return HttpResponseRedirect(request.path_info)
        soc_details['panno'] = request.POST.get('PAN_Number')
        soc_details['regno'] = request.POST.get('Registration_Number')
        soc_details['gstno'] = request.POST.get('GST_Number')
        soc_details['ctsno'] = request.POST.get('CTS_Number')
        soc_details['address'] = request.POST.get('address')
        request.session['soc_details'] = soc_details
        return redirect('/add_charges')      

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

def add_value(request):
    context={}
    selected_charges={}
    for key in request.POST:
        if request.POST[key] != ""  and request.POST[key] != "false":
            if request.POST[key] =='true':
                selected_charges[key] = ''
            else:
                selected_charges[key] = request.POST[key]
    selected_charges.pop("csrfmiddlewaretoken")
    context['selected_charges'] = selected_charges
    request.session['selected_charges'] = selected_charges
    return render(request,'add_value.html',context)

def persist_society_details(request):
    if request.method == "POST":
        selected_charges = request.session['selected_charges'] 
        soc_details = request.session['soc_details'] 
        user = request.user
        for key in selected_charges.keys():
            selected_charges[key] = request.POST[key]
        
        soc_details['user'] = user
        selected_charges['user'] = user
        soc_details['date_add_society'] = datetime.today()
        new_society = SocietyList(**soc_details)
        new_society.save()
        selected_charges['chargesSocietyName'] = SocietyList.objects.get(user = user , societyName=soc_details['societyName']) 
        selected_charges = DefaultChargesList(**selected_charges)
        selected_charges.save()
        return redirect('/society_detail')
    
def edit_society(request,name):
    edit_soc_details = SocietyList.objects.filter(user=request.user,societyName=name).values()
    context = {}
    context['soc_details'] = edit_soc_details[0]
    return render(request,'edit_society_details.html',context)

def save_edit_society(request,name):
    if request.method == "POST":
        soc_edit_details = {}
        for key in request.POST:
            soc_edit_details[key] = request.POST[key]
        soc_edit_details.pop('csrfmiddlewaretoken')
        SocietyList.objects.filter(user=request.user,societyName=name).update(**soc_edit_details)        
    return redirect('/society_detail')

def edit_charges(request,name):
    item = get_object_or_404(SocietyList,user=request.user, societyName=name)
    edit_charges = DefaultChargesList.objects.filter(user=request.user,chargesSocietyName=item).values()
    context={}
    selected_charges={}
    for key in edit_charges[0].keys():
        if edit_charges[0][key] != "":
            selected_charges[key] = edit_charges[0][key]
    rem_list = ['id','user_id','chargesSocietyName_id']
    for list_item in rem_list:
        selected_charges.pop(list_item)
    request.session['selected_charges']  = selected_charges
    context['selected_charges'] = selected_charges
    return render(request,'edit_charges.html',context)

def edit_value(request, name):
    context={}
    selected_charges={}
    for key in request.POST:
        if request.POST[key] != "" and request.POST[key] != "false":
            selected_charges[key] = request.POST[key]
    selected_charges.pop("csrfmiddlewaretoken")
    selected_charges_value = request.session['selected_charges'] 
    keys_list = list(set(list(selected_charges.keys()) + list(selected_charges_value.keys())))
    for item in keys_list:
        if item not in selected_charges.keys():
            selected_charges_value.pop(item)
    for item in selected_charges.keys():
        if item not in selected_charges_value.keys():
            selected_charges_value[item]=''    
    context['selected_charges'] = selected_charges_value
    request.session['selected_charges_value'] = selected_charges_value
    return render(request,'edit_value.html',context)

def edit_society_values(request,name):
    if request.method == "POST":
        item = get_object_or_404(SocietyList,user=request.user, societyName=name)
        selected_charges = request.session['selected_charges_value']
        for key in selected_charges.keys():
            selected_charges[key] = request.POST[key]
        DefaultChargesList.objects.filter(user = request.user , chargesSocietyName=item).update(**selected_charges) 
        return redirect('/society_detail')
    
def add_member(request,name):
    if request.method == "POST":
        mem_details = {}
        for key in request.POST.keys():
            mem_details[key] = request.POST[key]
        item = get_object_or_404(SocietyList,user=request.user, societyName=name)
        mem_details['memberSocietyName'] = item
        mem_details['user']=request.user
        mem_details.pop("csrfmiddlewaretoken")
        mem_details['date_add_member'] = datetime.today()
        add_member = MembersList(**mem_details)
        add_member.save()
        return redirect('/member_detail/' + name)
    return render(request,'add_member.html')

def member_detail(request, name):
    context = {}
    if name ==' ':
        item = get_object_or_404(SocietyList,user=request.user, societyName=SocietyList.objects.filter(user=request.user)[0].societyName)
    else:
        item = get_object_or_404(SocietyList,user=request.user, societyName=name)
    query_results = MembersList.objects.filter(user=request.user, memberSocietyName = item)
    society_list = SocietyList.objects.filter(user=request.user)
    context['query_results']=query_results
    context['society_list']=society_list
    return render(request, 'member_detail.html',context)

def deleteMember(request,memberSocietyName,building,FlatNo):
    item = get_object_or_404(SocietyList,user=request.user, societyName=memberSocietyName)
    MembersList.objects.filter(user=request.user, memberSocietyName = item, building = building, Flat_No=FlatNo ).delete()
    return redirect('/member_detail/' + memberSocietyName)

def editMember(request,memberSocietyName,building,FlatNo):
    item = get_object_or_404(SocietyList,user=request.user, societyName=memberSocietyName)
    edit_soc_details = MembersList.objects.filter(user=request.user,memberSocietyName=item,  building = building, Flat_No=FlatNo).values()
    context = {}
    edit_soc_details = edit_soc_details[0]
    edit_soc_details.pop('date_add_member')
    context['mem_details'] = edit_soc_details
    member_details = {}
    member_details['memberSocietyName'] = memberSocietyName
    member_details['building'] = building
    member_details['Flat_No'] = FlatNo
    request.session['member_details'] = member_details
    return render(request,'edit_member.html',context)

def update_member(request):
    if request.method == "POST":
        mem_details = {}
        for key in request.POST.keys():
            mem_details[key] = request.POST[key]
        sesion_mem_details = request.session['member_details']
        mem_details.pop('csrfmiddlewaretoken')
        item = get_object_or_404(SocietyList,user=request.user, societyName=sesion_mem_details['memberSocietyName'])
        MembersList.objects.filter(user=request.user,memberSocietyName=item,  building = sesion_mem_details['building'], Flat_No=sesion_mem_details['Flat_No']).update(**mem_details)
        return redirect('/member_detail/' + sesion_mem_details['memberSocietyName'])