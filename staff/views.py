from django.shortcuts import render
from django.contrib.auth.models import User
from django .http import HttpResponse
from django .http import HttpResponseRedirect
from customer.models import *
from customer.models import Staff, Category, Table, Reservation, Order, Menu, OrderMenu, Payments, Delivery, OrderDelivery, Reviews
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView


# Create your views here.
def dashboard(request):

    context = {
        'users': User.objects.all()
        
    }

    return render(request, 'dashboard.html', context)

class StaffList(ListView):
    model = Staff
    context_object_name = "staff"
    template_name = 'staff.html'

class CreateStaff(CreateView):
        model= Staff
        fields = ["name"]
        success_url = '/staff/staff'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Staff"

            return context
        
class StaffUpdate(UpdateView):
        model= Category
        fields = ["name"]
        success_url = '/staff/staff'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Staff"

            return context
        
class CategoryList(ListView):
    model = Category
    context_object_name = "category"
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
        fields = ["name"]
        success_url = '/staff/category'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Category"

            return context
        
class TableList(ListView):
    model = Table
    context_object_name = "table"
    template_name = 'table.html'

class CreateTable(CreateView):
        model= Table
        fields = ["name"]
        success_url = '/staff/table'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Table"

            return context
        
class TableUpdate(UpdateView):
        model= Table
        fields = ["name"]
        success_url = '/staff/table'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Table"

            return context

class ReservationList(ListView):
    model = Reservation
    context_object_name = "reservation"
    template_name = 'reservation.html'

class CreateReservation(CreateView):
        model= Reservation
        fields = ["name"]
        success_url = '/staff/reservation'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Reservation"

            return context
        
class ReservationUpdate(UpdateView):
        model= Reservation
        fields = ["name"]
        success_url = '/staff/reservation'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Reservation"

            return context

class   OrderList(ListView):
    model = Order
    context_object_name = "order"
    template_name = 'order.html'

class CreateOrder(CreateView):
        model= Order
        fields = ["name"]
        success_url = '/staff/order'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Order"

            return context
        
class OrderUpdate(UpdateView):
        model= Order
        fields = ["name"]
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
        fields = ["name"]
        success_url = '/staff/menu'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Menu"

            return context
        
class MenuUpdate(UpdateView):
        model= Menu
        fields = ["name"]
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
        fields = ["name"]
        success_url = '/staff/ordermenu'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create OrderMenu"

            return context
        
class OrderMenuUpdate(UpdateView):
        model= OrderMenu
        fields = ["name"]
        success_url = '/staff/ordermenu'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update OrderMenu"

            return context

class PaymentList(ListView):
    model = Payments
    context_object_name = "payment"
    template_name = 'payment.html'

class CreatePayment(CreateView):
        model= Payments
        fields = ["name"]
        success_url = '/staff/payment'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Payment"

            return context
        
class PaymentUpdate(UpdateView):
        model= Payments
        fields = ["name"]
        success_url = '/staff/payment'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Payment"

            return context


class DeliveryList(ListView):
    model = Delivery
    context_object_name = "delivery"
    template_name = 'delivery.html'

class CreateDelivery(CreateView):
        model= Delivery
        fields = ["name"]
        success_url = '/staff/delivery'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Delivery"

            return context
        
class DeliveryUpdate(UpdateView):
        model= Delivery
        fields = ["name"]
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
        fields = ["name"]
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
        fields = ["name"]
        success_url = '/staff/reviews'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Create Reviews"

            return context
        
class ReviewsUpdate(UpdateView):
        model= Reviews
        fields = ["name"]
        success_url = '/staff/reviews'
        template_name = 'staff_form.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = "Update Reviews"

            return context


        

        


        
