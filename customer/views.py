from datetime import datetime
from multiprocessing import context
import random
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
from django.views.generic import TemplateView, View
from django.contrib import messages



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
        'menu_items' : Menu.objects.all(),
        'categories' : Category.objects.all()

    }

    return render(request, 'menu_customer.html', context)



def makeOrder(request):
    food = Menu.objects.filter(type = Menu.FOOD)
    Drinks = Menu.objects.filter (type = Menu.DRINKS)
    print(food)

    

    context={
        'foods' : food,
        'drinks' : Drinks
       
        


    }

    return render(request, 'orders_form.html', context)

def saveOrder(request):
    ##Here you get all the form details
    phone_number = request.POST.get('phone_number')
    food = request.POST.get('food')
    drink = request.POST.get('drink')
    food_quantity = request.POST.get('food_quantity',1)
    drink_quantity = request.POST.get('drink_quantity',1)
    location = request.POST.get('location') 
    email = request.POST.get('email')
    

    cost = 0
    if food:
        selected_food = Menu.objects.filter(pk=food).first()
        cost = cost+(selected_food.price*float(food_quantity))
    if drink:
        selected_drink = Menu.objects.filter(pk=drink).first()
        cost = cost+(selected_drink.price*float(drink_quantity))

    current_user = User.objects.filter(email = email).filter(username=phone_number).first()
    if not current_user:
        current_user = User.objects.create_user(phone_number, email, email)

    ##After you get the details you create a new order order = Order.objects.create(...details...)
    ##Then you take them to the order details page
    order = Order.objects.create(
        user = current_user, 
        cost = cost,
        order_number = random.randint(0,999999)


    )

    if food:
        OrderMenu.objects.create(
            order = order,
            menu = selected_food,
            quantity = food_quantity
        )
    if drink:
        OrderMenu.objects.create(
            order = order,
            menu = selected_drink,
            quantity = drink_quantity
        )

    context ={
        

    ##Place the order you'l have created in this context so you can display it's details kwa the next page
    }
    return render(request, 'order_details.html', context)

## Main Dashboard page


## Documentation
class DocumentationView(View):

    def get(self, request):
        return render(request, "about.html")

def makeReservation(request):
    user_name=request.POST.get("name")
    email=request.POST.get("email")
    number_of_people = request.POST.get("people")
    date = request.POST.get("date")

    table = findTable()
    if not table:
        messages.info(request, 'Sorry. There are no available tables at the moment.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    current_user = User.objects.filter(email = email).first()
    if not current_user:
        current_user = User.objects.create_user(user_name, email, email)
    reservation=Reservation.objects.create(
        user=current_user,
        people = number_of_people,
        table = table,
        time = date
    )
    context= {
        "reservation":reservation
    }

    return HttpResponseRedirect('/reservation/complete')


def reservationComplete(request):

    '''
    This function will be used to redirect to the reservation confirmation page'''
    context = {}
    return render(request, "reservations_details.html", context)


def findTable(): 
    table = Table.objects.filter(is_taken=False).first()
    return table



           






