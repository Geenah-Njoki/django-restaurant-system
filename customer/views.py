from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import RandomForm, LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    context={

         "login_form" : LoginForm(),
        "register_form" : RegisterForm(),


    }
    return render(request, 'home.html', context)

def registerUser(request):
    if request.method== "GET":
        
        data = {'success': False, 
                'message':"Should be a POST request"}
        return JsonResponse(data)
    else:
        print(request.META)
        
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form. cleaned_data['name']
            
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User()
            user.username = name
            
            user.email = email
            user.set_password(password)
            user.save()

            login(request, user)
           
def loginUser(request):
    if request.method == 'GET':
        HttpResponse("Go home")
    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:

                login(request,user)
                context = {}

            

                return HttpResponseRedirect('/user/profile')
            else:
                messages.error(request, 'Login not successful')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
