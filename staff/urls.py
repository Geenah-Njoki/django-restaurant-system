from django.contrib import admin
from django.urls import path
from .views import *
from staff import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard', dashboard, name="dashboard"),
    path('staff', StaffList.as_view(), name="staff"),
    path('staff/create', CreateStaff.as_view(), name="create.staff"),
    path('staff/update/<pk>', StaffUpdate.as_view(), name= "staff.update"),
    path('category', CategoryList.as_view(), name="categories"),
    path('category/create', CreateCategory.as_view(), name="create.category"),
    path('category/update/<pk>', CategoryUpdate.as_view(), name= "category.update"),
    path('table', TableList.as_view(), name="table"),
    path('table/create', CreateTable.as_view(), name="create.table"),
    path('table/update/<pk>', TableUpdate.as_view(), name= "table.update"),
    path('reservation', ReservationList.as_view(), name="reservation"),
    path('reservation/create', CreateReservation.as_view(), name="create.reservation"),
    path('reservation/update/<pk>', ReservationUpdate.as_view(), name= "reservation.update"),
    path('order', OrderList.as_view(), name="order"),
    path('order/create', CreateOrder.as_view(), name="create.order"),
    path('order/update/<pk>', OrderUpdate.as_view(), name= "order.update")
]

