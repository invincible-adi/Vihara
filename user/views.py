from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import *

# Create your views here.
def index(request):
    return render(request,'user/index.html')

def join(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        joins(Name=name,Mobile=mobile,Email=email).save()
        return HttpResponse("<script>alert('You are join successfully')</script>")
    return render(request,'user/join.html')

def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        message=request.POST.get('message')
        x=contact(Name=name,Mobile=mobile,Email=email,Message=message).save()
       
        return HttpResponse("<script>alert('Thank you for contacting with us'); location.href='/user/contactus/' </script>")
    return render(request,'user/contactus.html')

def igallery(request):
    return render(request,'user/igallery.html')


def aboutus(request):
    return render(request,'user/aboutus.html')

def myevent(request):
    cid=request.GET.get('msg')
    sdata=request.GET.get('search')
    edata=event.objects.all().order_by('-id')
    md={
        "edata":edata
    }
    return render(request,'user/events.html',md)

def viewsdetails(request):
    eid=request.GET.get('msg')
    edata=event.objects.filter(id=eid)
    md={"edata":edata}
    return render(request,'user/viewsdetails.html',md)


def signin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        x=register.objects.filter(email=email,passwd=passwd).count()
        if x==1:
            a=register.objects.filter(email=email,passwd=passwd)
            request.session['username']=str(a[0].uname)
            request.session['userpic']=str(a[0].upic)
            request.session['user']=email
            return HttpResponse("<script>alert('You are Signed In'); location.href='/user/signin/'</script>")
        else:
            return HttpResponse("<script>alert('incorrect id & password');location.href='/user/signin/' </script>")
    return render(request,'user/signin.html')

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        address=request.POST.get('address')
        picture=request.FILES['fu']
        #print(name,email,passwd,address,picture)
        a=register.objects.filter(email=email).count()
        if a==0:
            register(email=email,uname=name,passwd=passwd,address=address,upic=picture).save()
            return HttpResponse("<script>alert('You are registered successfully...'); location.href='/user/signup/' </script>")

        else:
            return HttpResponse("<script>alert('You are already registered...'); location.href='/user/signup/' </script>")

        register(email=email,uname=name,passwd=passwd,address=address,upic=picture).save()
    return render(request,'user/signup.html')


def logout(request):
    user = request.session.get('user')
    if user:
        del request.session['user']
        return HttpResponse("<script>alert('You are logout successfully'); location.href='/user/index/'</script>")

    return render(request, 'user/logout.html')


def booking(request):
    user = request.session.get('user')
    if user:
        title = request.GET.get('title')
        price = request.GET.get('price')
        edate = request.GET.get('edate')
        epic = request.GET.get('epic')
        booknow(userid=user, event_name=title, event_picture=epic,event_date=edate, event_price=price, booking_date=datetime.now().date()).save()
        return HttpResponse("<script>alert('Your event is Successfully Booked'); location.href='/user/events/'</script>")
    else:
        return HttpResponse(
            "<script>alert('Firstly Signin your account '); location.href='/user/signin/'</script>")
    return render(request,'user/booking.html')

def myprofile(request):
    return render(request,'user/myprofile.html')

def vgallery(request):
    cid=request.GET.get('x')
    cdata=category.objects.all().order_by('-id')
    if cid is not None:
        vdata=videogallery.objects.filter(category=cid)
    else:
        vdata=videogallery.objects.all().order_by('-id')
    mydict={
        "cdata":cdata,
        "vdata":vdata,
    }
    return render(request,'user/vgallery.html',mydict)