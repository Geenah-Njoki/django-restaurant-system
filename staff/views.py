from django.shortcuts import render
from django.contrib.auth.models import User
from django .http import HttpResponse, JsonResponse
from django .http import HttpResponseRedirect
from customer.models import *
from customer.models import Staff, Category, Table, Reservation, Order, Menu, OrderMenu, Payments, Delivery, OrderDelivery, Reviews
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


# Create your views here.
@login_required
def dashboard(request):

    context = {
        'users': User.objects.all()
        
    }

    return render(request, 'dashboard.html', context)
@login_required
def viewStaff(request):
    context = {
        'staff' : Staff.objects.all()
    }

    return render(request, 'staff.html', context)

@login_required
def deleteStaff(request, id):

    staff = Staff.objects.get(pk=id)
    staff.delete()

    

    if request.is_ajax():

        data = {}
        return JsonResponse(data)

    else:
        return HttpResponseRedirect('/staff/staff')

@login_required
def viewMenu(request):
    context = {
        'menu' : Menu.objects.all()
    }

    return render(request, 'menu.html', context)

@login_required
def deleteMenu(request, id):

    menu = Menu.objects.get(pk=id)
    menu.delete()

    

    if request.is_ajax():

        data = {}
        return JsonResponse(data)

    else:
        return HttpResponseRedirect('/staff/menu')

@login_required
def viewPayment(request):
    context = {
        'payment' : Payments.objects.all()
    }

    return render(request, 'payment.html', context)

@login_required
def viewReview(request):
    context = {
        'reviews' : Reviews.objects.all()
    }

    return render(request, 'reviews.html', context)

@login_required
def deleteReview(request, id):

    review = Reviews.objects.get(pk=id)
    review.delete()

    

    if request.is_ajax():

        data = {}
        return JsonResponse(data)

    else:
        return HttpResponseRedirect('/staff/reviews')
@login_required
def deleteReservation(request, id):

    reservation = Reservation.objects.get(pk=id)
    reservation.delete()

    

    if request.is_ajax():

        data = {}
        return JsonResponse(data)

    else:
        return HttpResponseRedirect('/staff/reservation')


# @login_required

# def viewDelivery(request):
#     context = {
#         'delivery' : Delivery.objects.all()
#     }

#     return render(request, 'delivery.html', context)

class StaffList(ListView):
    model = Staff
    context_object_name = "staff_list"
    template_name = 'staff.html'

class CreateStaff(CreateView):
        model= Staff
        fields = ["username","staff_number","gender", "salary", "address","department", "working_hours"]
        success_url = '/staff/staff'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Staff"

            return context
        
class StaffUpdate(UpdateView):
        model= Staff
        fields = '__all__'
        success_url = '/staff/staff'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Staff"

            return context

class StaffDetails(DetailView):
    model = Staff
    template_name = 'staff_details.html'
    context_object_name = "staff"
        
class CategoryList(ListView):
    model = Category
    context_object_name = "categories"
    template_name = 'categories.html'

class CreateCategory(CreateView):
        model= Category
        fields = ["name"]
        success_url = '/staff/category'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Category"

            return context
        
class CategoryUpdate(UpdateView):
        model= Category
        fields = "__all__"
        success_url = '/staff/category'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Category"

            return context
        
class TableList(ListView):
    model = Table
    context_object_name = "tables"
    template_name = 'table.html'

class CreateTable(CreateView):
        model= Table
        fields = ["table_number", "is_taken"]
        success_url = '/staff/table'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Table"

            return context
        
class TableUpdate(UpdateView):
        model= Table
        fields = "__all__"
        success_url = '/staff/table'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Table"

            return context

class ReservationList(ListView):
    model = Reservation
    context_object_name = "reservations"
    template_name = 'reservation.html'

class CreateReservation(CreateView):
        model= Reservation
        fields = ["table","user", "people", "status"]
        success_url = '/staff/reservation'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Reservation"

            return context
        
class ReservationUpdate(UpdateView):
        model= Reservation
        fields = "__all__"
        success_url = '/staff/reservation'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Reservation"

            return context

class ReservationDetails(DetailView):
    model = Reservation
    template_name = 'reservation_details.html'
    context_object_name = "reservation"

class   OrderList(ListView):
    model = Order
    context_object_name = "orders"
    template_name = 'order.html'

class CreateOrder(CreateView):
        model= Order
        fields = ["status","cost","user", "is_delivery", "order_number", "staff"]
        success_url = '/staff/order'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Order"

            return context
        
class OrderUpdate(UpdateView):
        model= Order
        fields = "__all__"
        success_url = '/staff/order'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Order"

            return context
        
class MenuList(ListView):
    model = Menu
    context_object_name = "menu"
    template_name = 'menu.html'

class CreateMenu(CreateView):
        model= Menu
        fields = ["type", "category", "item", "quantity"]
        success_url = '/staff/menu'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Menu"

            return context
        
class MenuUpdate(UpdateView):
        model= Menu
        fields = '__all__'
        success_url = '/staff/menu'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Menu"

            return context

class OrderMenuList(ListView):
    model = OrderMenu
    context_object_name = "ordermenu"
    template_name = 'ordermenu.html'

class CreateOrderMenu(CreateView):
        model= OrderMenu
        fields = "__all__"
        success_url = '/staff/ordermenu'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create OrderMenu"

            return context
        
class OrderMenuUpdate(UpdateView):
        model= OrderMenu
        fields = "__all__"
        success_url = '/staff/ordermenu'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update OrderMenu"

            return context
class MenuDetails(DetailView):
    model = Menu
    template_name = 'menu_details.html'
    context_object_name = "menu"

class PaymentList(ListView):
    model = Payments
    context_object_name = "payments"
    template_name = 'payment.html'

class CreatePayment(CreateView):
        model= Payments
        fields = ["status", "user", "order", "payment_mode"]
        success_url = '/staff/payment'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Payment"

            return context
        
class PaymentUpdate(UpdateView):
        model= Payments
        fields = '__all__'
        success_url = '/staff/payment'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Payment"

            return context
class PaymentDetails(DetailView):
    model = Payments
    template_name = 'payment_details.html'
    context_object_name = "payments"


class DeliveryList(ListView):
    model = Delivery
    context_object_name = "deliveries"
    template_name = 'delivery.html'

class CreateDelivery(CreateView):
        model= Delivery
        fields = ["location_groups", "delivery_fee"]
        success_url = '/staff/delivery'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Delivery"

            return context
        
class DeliveryUpdate(UpdateView):
        model= Delivery
        fields = '__all__'
        success_url = '/staff/delivery'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Delivery"

            return context
        
class OrderDeliveryList(ListView):
    model = OrderDelivery
    context_object_name = "orderdelivery"
    template_name = 'orderdelivery.html'

class CreateOrderDelivery(CreateView):
        model= OrderDelivery
        fields = ["name"]
        success_url = '/staff/orderdelivery'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create OrderDelivery"

            return context
        
class OrderDeliveryUpdate(UpdateView):
        model= OrderDelivery
        fields = "__all__"
        success_url = '/staff/orderdelivery'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update OrderDelivery"

            return context

class ReviewsList(ListView):
    model = Reviews
    context_object_name = "reviews"
    template_name = 'review.html'

class CreateReviews(CreateView):
        model= Reviews
        fields = ["user", "message", "stars"]
        success_url = '/staff/reviews'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Reviews"

            return context

class ReviewDetails(DetailView):
    model = Reviews
    template_name = 'review_details.html'
    context_object_name = "review"
        
class ReviewsUpdate(UpdateView):
        model= Reviews
        fields = "__all__"
        success_url = '/staff/reviews'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Reviews"

            return context


        

        


        
