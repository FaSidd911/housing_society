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
from .forms import ChargesForm,MembersForm,EditSocietyForm
import json

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
                return render(request, "addSociety.html",{'query_results':query_results})
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
            return HttpResponseRedirect('societyMembers')
        new_member = MembersList(**members_dict)
        new_member.save() 
        return HttpResponseRedirect(request.path_info)
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
                print(societyNameExists)
                if societyNameExists:
                    return HttpResponseRedirect(request.path_info)
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

def deleteSociety(request,name):
    SocietyList.objects.filter(user=request.user,societyName=name).delete()
    return HttpResponseRedirect('/addSociety')