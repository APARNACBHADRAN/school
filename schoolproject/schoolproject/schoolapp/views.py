
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import schoolForms
from .models import student


# Create your views here.
def demo(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("username="+username)
        print("Password="+password)
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            print("valid")
            auth.login(request,user)
            return redirect("/hello")
        else:
            print("invalid credentials")
            messages.info(request, "invalid credentials")
            return redirect("/login")
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        conpassword=request.POST['cpassword']
        if password==conpassword :
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username,password=password)
                print("user created")
                user.save();
                return redirect('/login')
        else:
             messages.info(request,"Password mismatch")
             return redirect('/register')
        return redirect('/')
    return render(request,"register.html")
def hello(request):
    return render(request,'hello.html')

def form_order(request):
    form = schoolForms(request.POST or None)
    #
    if form.is_valid():
         form.save()
    print("hello")
    purpose=request.POST.get('purpose',False)
    # messages.success(request,purpose)
    print(purpose)

        # return redirect('/')
    return render(request,'form_order.html',{'purpose':purpose,'f1':form})

def logout(request):
    auth.logout(request)
    return redirect('/')
def submit(request):
    print("hello")
    purpose = request.POST.get('purpose', False)
    messages.success(request, purpose)

    print(messages)
    return render(request,'message.html',{'messages':messages})