from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import datetime
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .decorators import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import get_object_or_404
from datetime import date

# @login_required(login_url='/')
def index(request):
    visitor = VisitDetails.objects.all().order_by('-visit_id')
    return render(request,'basic/dashboard.html',{'visitor':visitor,'k':True})

@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin'])
def host(request):
    host =Host.objects.all().order_by('host_id')
    count = host.count()
    return render(request,'basic/host.html',{'host':host,'count':count,'k':False})
# def hostdynamic(request,pk):
#     host1 = Host.objects.get(host_id=pk)
#     return render(request,'basic/hostdynamic.html',{'host':host1,'k':False})

@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin'])
def createhost(request):
    form=HostForm1()
    form1=createuserform()
    if request.method == 'POST': 
        form=HostForm1(request.POST)
        form1=createuserform(request.POST)
        h = Host.objects.all()
        a= []
        for i in h:
            a.append(i.flat_no)
        print(a)
        check = int(request.POST['flat_no'])
        if check not in a:
            if form1.is_valid() and form.is_valid(): 
                email = request.POST['email']
                Phone_no = request.POST['Phone_no']
                flat_no = request.POST['flat_no']
                age =      request.POST['age']
                gender =      request.POST['gender']
                no_of_people = request.POST['no_of_people']
                name = request.POST['name']
                user=form1.save()
                host = Host(user=user,name=name,age=age,gender=gender,email_id=email,no_of_people=no_of_people,flat_no=flat_no,Phone_no=Phone_no)
                host.save()
                group = Group.objects.get(name='host')
                user.groups.add(group)
                host =Host.objects.all().order_by('host_id')
                count = host.count()
                return render(request,'basic/host.html',{'host':host,'count':count,'k':False})
            else:
                return render(request,'basic/create_host.html',{"form":form,"form1":form1,"email_check_msg":"Enter unique email","age_msg":"Minimum age required is 21","phone_no_msg":"Enter valid phone number(with 10 digits)","no_of_people_msg":"Number of residents should be less than 5","error":"Please use a Unique Username or a stronger Password and enter valid data for Signup","message1":"Your password can’t be too similar to your other personal information.","message2": "Your password must contain at least 4 characters","message3":"Your password can’t be a commonly used password."})
        else:
            messages.error(request,'Flat no is not unique')
    context={'form1':form1,'k':False,'S':True,'form':form,"email_check_msg":"Enter unique email","age_msg":"Minimum age required is 21 ","phone_no_msg":"Enter valid phone number(with 10 digits)","no_of_people_msg":"Number of residents should be less than 5","message1":"Your password can’t be too similar to your other personal information.","message2": "Your password must contain at least 4 characters","message3":"Your password can’t be a commonly used password."}
    return render(request,'basic/create_host.html',context)
# @admin_only
@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin'])
def updateHost(request,id=None):
    host = Host.objects.get(host_id=id)
    form = HostForm1(instance=host)
    if request.method == 'POST':
        form = HostForm1(request.POST,request.FILES,instance=host)
        if form.is_valid():
            form.save()
            host =Host.objects.all().order_by('host_id')
            count = host.count()
            return render(request,'basic/host.html',{'host':host,'count':count,'k':False,'S':False})   
        else:
            return render(request,'basic/update_host.html',{"form":form,"error":"Please enter valid data to update Host","age_msg":"Minimum age required is 21","phone_no_msg":"Enter valid phone number(with 10 digits)","no_of_people_msg":"Number of residents should be less than 5"})
    context={'form':form,'k':False,'S':False,"phone_no_msg":"Enter valid phone number(with 10 digits)","age_msg":"Minimum age required is 21","no_of_people_msg":"Number of residents should be less than 5"}
    return render(request,'basic/update_host.html',context)


@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin'])
def deleteHost(request,pk):
    host = Host.objects.get(host_id=pk)
    if request.method == "POST":
        host.delete()
        host =Host.objects.all().order_by('host_id')
        count = host.count()
        return render(request,'basic/host.html',{'host':host,'count':count,'k':False})
    return render(request,'basic/delete_host.html',{'form':host,'k':False})



@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin','entryperson'])
def visitor(request):
    visitor = Visitor.objects.all().order_by('-visitor_id')
    return render(request,'basic/visitor.html',{'visitor':visitor,'k':False})

@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin','entryperson'])
def createvisitor(request):
    form = VisitorForm()
    if request.method == 'POST':
        form = VisitorForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            visitor = Visitor.objects.all().order_by('-visitor_id')
            return render(request,'basic/visitor.html',{'visitor':visitor,'k':False}) 
    context={'form':form,'k':False}
    return render(request,'basic/create_visitor.html',context)

@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin','entryperson'])
def updatevisitor(request,pk):
    visitor = Visitor.objects.get(visitor_id=pk)
    form = VisitorForm(instance=visitor)
    if request.method == 'POST':
        form = VisitorForm(request.POST,request.FILES,instance=visitor)
        if form.is_valid():
            form.save()
            visitor = Visitor.objects.all().order_by('-visitor_id')
            return render(request,'basic/visitor.html',{'visitor':visitor,'k':False})
    context={'form':form,'k':False}
    return render(request,'basic/create_visitor.html',context)

@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin'])
def deletevisitor(request,pk):
    visitor = Visitor.objects.get(visitor_id=pk)
    if request.method == "POST":
        visitor.delete()
        visitor = Visitor.objects.all().order_by('-visitor_id')
        return render(request,'basic/visitor.html',{'visitor':visitor,'k':False})
    return render(request,'basic/delete_visitor.html',{'form':visitor,'k':False}) 




@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin'])
def events(request):
    complete =0
    event = Event.objects.all()
    upcomming = event.count()
    for i in event:
        a = i.tag
        if a == 'Complete':
            complete +=1
            i.option1 = True
            i.option2 = False
        else:
            i.option1 = False
            i.option2 = True
    upcomming = upcomming - complete
    return render(request,'basic/events.html',{'form':event,'complete':complete,'upcomming':upcomming})

@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin','host'])
def createevent(request):
    form =EventForm()
    if request.method == 'POST':
        group = request.user.groups.all()[0].name
        if group == 'host':
            organizer= Host.objects.filter(user = request.user)
            tag =request.POST['tag']
            event_date_time = request.POST['event_date_time']
            event_purpose = request.POST['event_purpose']
            event_date_time= str(event_date_time)
            date_object = datetime.strptime(event_date_time, '%Y-%m-%d').date()
            if date.today() >=date_object :
                messages.success(request,f"Got wrong input date")
                return render(request,'basic/create_event.html',{'form':form,'k':False,"date_msg":"Please enter valid date"})
            for i in organizer:
                org = i
            try:
                event = Event(tag=tag,organizer=org,event_date_time=event_date_time,event_purpose=event_purpose)
                event.save()
            except:
                messages.error(request,f"Other organizer created event on same day .Please contact admin or change date for event")


        if group != 'host':
            organizer= int(request.POST['organizer'])
            organizer = Host.objects.filter(host_id=organizer)
            tag =request.POST['tag']
            event_date_time = request.POST['event_date_time']
            event_purpose = request.POST['event_purpose']
            event_date_time= str(event_date_time)
            date_object = datetime.strptime(event_date_time, '%Y-%m-%d').date()
            if date.today() >=date_object :
                  return render(request,'basic/create_event.html',{'form':form,'k':False,"date_msg":"Please enter valid date"})
            
            for i in organizer:
                org = i
            try:
                event = Event(tag=tag,organizer=org,event_date_time=event_date_time,event_purpose=event_purpose)
                event.save()
            except:
                messages.error(request,f"Other organizer created event on same day ")
                messages.error(request,f"Contact the admin for more details ")
        # form = EventForm(request.POST)
        # if form.is_valid():
        #     form.save()
        complete =0
        event = Event.objects.all()
        upcomming = event.count()
        for i in event:
            a = i.tag
            if a == 'Complete':
                complete +=1
                i.option1 = True
                i.option2 = False
            else:
                i.option1 = False
                i.option2 = True
        upcomming = upcomming - complete
        group = request.user.groups.all()[0].name
        if group == 'host':
            return redirect('/user')
        elif group != 'host':
            return render(request,'basic/events.html',{'form':event,'complete':complete,'upcomming':upcomming})
    return render(request,'basic/create_event.html',{'form':form,'k':False,"check_msg":"One Host can create only one event for a day"})

@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin','host'])
def updateevent(request,pk):
    event = Event.objects.get(event_id=pk)
    form = EventForm(instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            event = Event.objects.all()
            group = request.user.groups.all()[0].name
            if group == 'host':
                return redirect('/user')
            if group != 'host':
                return redirect('/events',{'form':event,'k':False})
            return render(request,'basic/events.html',{'form':event,'k':False})
    context={'form':form,'k':False}
    return render(request,'basic/create_event.html',context)
@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin','host'])
def deleteevent(request,pk):
    event = Event.objects.get(event_id=pk)
    if request.method == "POST":
        event.delete()
        group = request.user.groups.all()[0].name
        if group == 'host':
            return redirect('/user')
        event = Event.objects.all()
        return render(request,'basic/events.html',{'form':event,'k':False})
    return render(request,'basic/delete_event.html',{'form':event,'k':False}) 





@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin','entryperson'])
def visitdetails(request):
    form = VisitDetailsForm()
    visitdetail = VisitDetails.objects.all()
    count = visitdetail.count()
    date_object = date.today()
    date_object = str(date_object)
    count = 0
    for i in visitdetail:
        a = i.visit_date
        day = a.day
        month = a.month
        year = a.year
        if day <10:
            day = str(0)+str(day)
        if month<10:
            month = str(0)+str(month)
        date1 = str(year)+str('-')+str(month)+str('-')+str(day)
        if date_object == date1:
            count =count +1
    if request.method == 'POST':
        a = request.POST
        a1=a['duration']
        a2=a['purpose']
        a3=a['visit_detail']
        a4=a['flat_no']
        check = Host.objects.all()
        k = []
        for i in check:
            k.append(i.flat_no)
        if int(a4) in k:
            a3 = Visitor.objects.get(visitor_id=a3)
            visitdetails = VisitDetails(duration=a1,purpose=a2,visit_detail=a3,flat_no=a4)
            visitdetails.save()
            # messages.success(request,"visit entered successfull")
            return redirect('/')
        else:
            messages.error(request,'That flat number is not allocated or entered wrong detail')
    context={'form':form,'count':count,'k':False}
    return render(request,'basic/visitdetails.html',context)




@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin','entryperson'])
def eventvisitor(request):
    form =EventVisitorForm()
    if request.method == 'POST':
        form = EventVisitorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Event guest  entered successfull")
            form =EventVisitorForm()
            return render(request,'basic/eventvisitor.html',{'form':form,'k':False})
    return render(request,'basic/eventvisitor.html',{'form':form,'k':False})


# @unauthenticated_user
# def handleSignup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
#         myuser = User.objects.create_user(username,email,pass1)
#         myuser.first_name = fname
#         myuser.last_name = lname
#         myuser.save()

#         host = Host(user=myuser,name=str(str(fname)+str(lname)),email_id=email)
#         host.save()
#         group = Group.objects.get(name='host')
#         myuser.groups.add(group)


#         messages.success(request,'Account have be created')
#         redirect('/')
#     visitor = VisitDetails.objects.all().order_by('-visit_id')
#     return render(request,'basic/dashboard.html',{'visitor':visitor,'k':True})

@unauthenticated_user
def handlelogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password=password)
        if user is not None:
            login(request,user)
            group = request.user.groups.all()[0].name
            if group == 'host':
               return redirect('/user')
            if group != 'host':
                return redirect('/') 
        else:
            messages.error(request,'Credential wrong')
            visitor = VisitDetails.objects.all().order_by('-visit_id')
            return render(request,'basic/dashboard.html',{'visitor':visitor,'k':True})
    visitor = VisitDetails.objects.all().order_by('-visit_id')
    return render(request,'basic/dashboard.html',{'visitor':visitor,'k':True})

def handlelogout(request):
    logout(request)
    return redirect('/')
        

@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin','host'])
def userpage(request):
    a = request.user
    try:
        host = Host.objects.get(user=a)
    except:
        host = None
    if host is not None:
        k = []
        bst=[]
        b = 'b'
        forms = Event.objects.all()
        for i in forms:
            if str(i.organizer) == str(host.name)+"(flat number"+str(host.flat_no)+")":
                k.append(i.event_id)
        for i in range(len(k)):
            b = b+str(i)
            a = Event.objects.get(event_id = k[i])
            bst.append(a)
            b = 'b'
        return render(request,'basic/user.html',{'form':bst})
    else:
        return  render(request,'basic/user.html',{'form':''})



@login_required(login_url='/')
@allowed_users(allowed_roles = ['admin','host'])
def accountsettings(request):
    user = request.user.host
    form = HostForm1(instance=user)
    if request.method == 'POST':
        a = request.POST['age']
        a = int(a)
        if a>100:
            messages.error(request,'Age is invalid input')
        else:
            try:
                # print(request.POST)
                form = HostForm(request.POST,request.FILES,instance=user)
                form.save()
                messages.success(request,f"Account successfully updated ")
            except Exception as e:
                user = request.user.host
                form = HostForm1(instance=user)
                messages.error(request,f'error message is {e}')
                return render(request,'basic/account_settings.html',{'form':form})

    return render(request,'basic/account_settings.html',{'form':form})

@login_required(login_url='/')
@allowed_users(allowed_roles = ['host'])
def analysispage(request,pk):
    name = Event.objects.get(event_id=pk)
    people = EventVisitor.objects.filter(event_info=name)
    return render(request,'basic/analysispage.html',{'people':people,'event':name})
