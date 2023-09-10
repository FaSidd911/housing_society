from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth import  authenticate #add this
from django.contrib.auth import login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime
from .models import SocietyList,MembersList,DefaultChargesList,MemberChargesList
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .forms import ChargesForm,MembersForm,EditSocietyForm,EditMembersForm
import json,os
import pandas as pd
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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
        charges_list = ['Member_Name', 'Flat_No', 'building', 'Contact_Number', 'Balance', 'PAN_Number', 'Aadhar_Number']
        for key in selected_charges.keys():
            selected_charges[key] = request.POST[key]
            charges_list.append(key)
        soc_details['user'] = user
        selected_charges['user'] = user
        soc_details['date_add_society'] = datetime.today()
        new_society = SocietyList(**soc_details)
        new_society.save()
        selected_charges['chargesSocietyName'] = SocietyList.objects.get(user = user , societyName=soc_details['societyName']) 
        selected_charges = DefaultChargesList(**selected_charges)
        selected_charges.save()
        path = settings.MEDIA_ROOT + '/' + request.user.username + '/' +  soc_details['societyName']
        if not os.path.exists(path):
            os.makedirs(path)
        df = pd.DataFrame(columns=charges_list)
        df.to_csv(path + r'/Member_Details.csv',index=False)
        del request.session['soc_details']
        del request.session['selected_charges']
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
        del request.session['selected_charges_value']
        del request.session['selected_charges']
        return redirect('/society_detail')
    
def add_member(request,name):
    context={}
    context['name']= name
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
    return render(request,'add_member.html',context )

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
    context['name'] = name
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
    context['name']=memberSocietyName
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
        del request.session['member_details']
        return redirect('/member_detail/' + sesion_mem_details['memberSocietyName'])
    
def import_members(request,name):
    context={}
    context['name']  = name
    if request.method == 'POST':
        item = get_object_or_404(SocietyList,user=request.user, societyName=name)
        members_list_df = pd.read_csv(request.FILES['others'],index_col=False)
        members_list_df = members_list_df.loc[:, ~members_list_df.columns.str.match('Unnamed')]
        rem_list = ['Member_Name', 'Flat_No', 'building', 'Contact_Number', 'Balance', 'PAN_Number', 'Aadhar_Number']
        mem_details_dict = members_list_df.to_dict(orient='records')
        for mem_item in mem_details_dict:
            charges_dict = mem_item.copy()
            member_dict = mem_item.copy()
            for key in rem_list:
                del charges_dict[key]
            for key  in rem_list:
                if key not in rem_list:
                    del member_dict[key]
            del_keys = [ key for key in member_dict if key not in rem_list ]
            for key in del_keys:
                del member_dict[key]
            member_dict['user'] = request.user
            member_dict['memberSocietyName'] = item
            member_dict['date_add_member'] = datetime.today()
            add_member = MembersList(**member_dict)
            add_member.save()
            Member_item = get_object_or_404(MembersList,user=request.user, memberSocietyName=item, Member_Name=member_dict['Member_Name'])
            charges_dict['user'] = request.user
            charges_dict['chargesSocietyName'] = item
            charges_dict['chargesMemberName'] = Member_item
            add_charges= MemberChargesList(**charges_dict)
            add_charges.save()
        return redirect('/member_detail/' + name)
    return render(request, 'import_members.html',context )

def download_file(request, name):
    path = settings.MEDIA_ROOT + '/' + request.user.username + '/' + name + '/Member_Details.csv'
    response = HttpResponse(open(path, 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename=' + name + '.csv'
    return response

def upload_doc(request,name):
    path = settings.MEDIA_ROOT + '/' + request.user.username + '/' +  name
    if not os.path.exists(path):
            os.makedirs(path)
    fs = FileSystemStorage(path)   
    files = os.listdir(path)
    file_names = {'pan':' ',
                  'gst':' ',
                  'cts':' ',
                  'oth':' '}
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
        'file_names':file_names,
        'name':name
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

def download_doc(request, name, doc):
    path = settings.MEDIA_ROOT + '/' + request.user.username + '/' + name + '/' + doc
    response = HttpResponse(path)
    response['Content-Type'] = 'image/jpeg'
    response['Content-Disposition'] = 'attachment; filename=' + doc
    return response

def show_member_detail(request):
    return render(request,'show_member_detail.html')

def charges_detail(request, name):
    context = {}
    if name ==' ':
        item = get_object_or_404(SocietyList,user=request.user, societyName=SocietyList.objects.filter(user=request.user)[0].societyName)
    else:
        item = get_object_or_404(SocietyList,user=request.user, societyName=name)
    query_results = MembersList.objects.filter(user=request.user, memberSocietyName = item)
    mem_chg_details = {}
    for soc_members in query_results:
        mem_chg_details['Member_Name'] = soc_members.Member_Name
        mem_chg_details['building'] = soc_members.building
        mem_chg_details['Flat_No'] = soc_members.Flat_No
        mem_chg_details['Balance'] = soc_members.Balance
    query_results = DefaultChargesList.objects.filter(user = request.user , chargesSocietyName=item)
    for soc_chg in query_results:
        fields =  soc_chg._meta.get_fields()
        for i in fields:
            if i.attname not in ['id', 'user_id', 'chargesSocietyName_id']:
                if getattr(soc_chg, i.attname) != '':
                    mem_chg_details[i.attname] = getattr(soc_chg, i.attname)         
    society_list = SocietyList.objects.filter(user=request.user)
    context['mem_chg_details']=mem_chg_details
    context['society_list']=society_list
    context['name'] = name
    return render(request, 'charges_detail.html',context)
