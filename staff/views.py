from django.shortcuts import render
from django.contrib.auth.models import User
from django .http import HttpResponse
from django .http import HttpResponseRedirect
from customer.models import *
from customer.models import Staff, Category, Table, Reservation, Order
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
        

        
