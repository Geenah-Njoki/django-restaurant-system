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
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .models import *

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


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset_confirm.html", context={"password_reset_form":password_reset_form})
    
def password_reset_requuest(request):

    password_reset_form = PasswordResetForm(request.POST)
    if password_reset_form.is_valid():
        data = password_reset_form.cleaned_data['email']

        send_mail(
            'Ssup',
            'Reset Jamaa',
            'gg@gmail.com',
            [data],
            fail_silently=False,
        )

        return render(request=request, template_name="password/password_reset_confirm.html", context={})

def getOrders(request):
    
    context={
        'orders' : Order.objects.all()

    }
    
    return render(request, 'orders.html', context)

def getReservations(request):
    context={
        'reservations' : Reservation.objects.all()

    }

    return render(request, 'reservations.html', context)

def getReviews(request):
    context={
        'reviews' : Reviews.objects.all()

    }

    return render(request, 'reviews.html', context)

def getMenu(request):
    context={
        'menu' : Menu.objects.all()

    }

    return render(request, 'menu.html', context)








