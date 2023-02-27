from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .mixin import *
from .models import *
import random
from django.contrib.auth import logout
# Create your views here.


def home(request):
    return render(request, 'index.html')



def login(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        
        profile = Profile.objects.get(mobile = mobile)
        
        if profile is None:
            context = {'error' : 'User not found register first' }
            return render(request,'signup.html' , context)
        
        profile.otp = str(random.randint(1000 , 9999))
        profile.save()

        message_handler = MessaHandler(mobile, profile.otp).send_otp_on_phone()
        return redirect(f'/otp/{profile.mobile}')     
       
    return render(request,'login.html')



def logout_user(request):
    logout(request)
    return redirect("/login")



def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('username')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            context = {'error':"Password Don't Match"}
            return render(request,'signup.html')

        check_user = User.objects.filter(email = email).first()
        check_profile = Profile.objects.filter(mobile = mobile).first()
        
        if check_user or check_profile:
            context = {'error' : 'User already exists'}
            return render(request,'register.html' , context)
        
        if not mobile.__contains__('+'):
        
            context = {'error' : 'Enter Number in Format +(country-code)(number)'}
            return render(request,'signup.html' , context)
            
        user = User.objects.create(email = email ,username = name, password = password)
        Profile.objects.create(user = user , mobile=mobile)
        # mobile = ""
        # # send_otp(mobile, otp)
        return redirect('/login')
    
    return render(request,'signup.html')



def otp(request,mobile):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.get(mobile=mobile)
        
        if otp == profile.otp:
            return redirect('/')
        else:
            print('Wrong')
            
            context = {'error' : 'Wrong OTP' ,'mobile':mobile }
            return render(request,'otp.html' , context)
            
        
    return render(request,'otp.html')