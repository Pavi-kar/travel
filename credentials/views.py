from django.contrib import messages, auth
from django.contrib.auth.models import User


from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        u_name=request.POST['username']
        p_word=request.POST['password']
        user=auth.authenticate(username=u_name,password=p_word)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials!")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        e_mail = request.POST['email']
        pwd = request.POST['password']
        cpwd = request.POST['password1']
        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username already taken!')
                return redirect('register')
            elif User.objects.filter(email=e_mail).exists():
                messages.info(request,'Email already registered!')
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=pwd,first_name=f_name,last_name=l_name,email=e_mail)
                user.save();
                print("User Created!")
                return redirect('login')

        else:
            messages.info(request,"Password not matched!!!")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        passwd=request.POST['password']
        user=auth.authenticate(username=uname,password=passwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials!")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
