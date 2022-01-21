from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'inavlid credentials')
            return redirect('login')
    else:
     return render(request,'login.html')

def register(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        pswd1=request.POST['password1']
        pswd2=request.POST['password2']
        email=request.POST['email']
        if pswd1==pswd2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username, password=pswd1, email=email,first_name=fname,last_name=lname)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matched')
            return redirect('register')
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect("/")