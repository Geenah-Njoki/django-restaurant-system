"""restaurant_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from customer import views
from django.views.generic import TemplateView, View
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', home, name="home"),
    path('send/reset/email', password_reset_request, name="send_reset_email"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password/password-reset-done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password-reset-confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password-reset-complete.html'), name='password_reset_complete'),    
    path('customer/orders', views.getOrders, name="customer.orders"),
    path('customer/reservations', views.getReservations, name='customer.reservations'),
    path('customer/reviews', views.getReviews, name="customer.reviews"),
    path('customer/menu', views.getMenu, name="customer.menu"),
    path('customer/order', views.makeOrder, name="customer.order"),
    path('customer/make/order', views.saveOrder, name='save.order'),
    path('customer/about', DocumentationView.as_view(), name="customer.about"),
    path('customer/order_details', TemplateView.as_view(template_name='order_details.html'), name="order_details"),
    path('customer/make/reservations', views.makeReservation, name="customer.make.reservations"),
    path('reservation/complete', views.reservationComplete, name="reservation.complete"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  