from django.contrib import admin
from django.urls import path
from .views import *
from staff import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard', dashboard, name="dashboard"),

    path('user/create', CreateUser.as_view(), name="create.user"),

    path('staff', StaffList.as_view(), name="staff"),
    path('staff', viewStaff, name='staff'),
    path('staff/create', CreateStaff.as_view(), name="create.staff"),
    path('staff/update/<pk>', StaffUpdate.as_view(), name= "staff.update"),
    path('staff/<pk>/details', StaffDetails.as_view(), name="staff.details"),
    path('staff/delete/<int:id>', deleteStaff, name="staff.delete"),
   
    path('category', CategoryList.as_view(), name="categories"),
    path('category/create', CreateCategory.as_view(), name="create.category"),
    path('category/update/<pk>', CategoryUpdate.as_view(), name= "category.update"),
    path('category/<pk>/details', CategoryDetails.as_view(), name="category.details"),
    path('category/delete/<int:id>', deleteCategory, name="category.delete"),

    path('table', TableList.as_view(), name="table"),
    path('table', viewTable, name='table'),
    path('table/create', CreateTable.as_view(), name="create.table"),
    path('table/update/<pk>', TableUpdate.as_view(), name= "table.update"),
    path('reservation', ReservationList.as_view(), name="reservation"),
    path('reservation/create', CreateReservation.as_view(), name="create.reservation"),
    path('reservation/<pk>/details', ReservationDetails.as_view(), name="reservation.details"),
    path('reservation/update/<pk>', ReservationUpdate.as_view(), name= "reservation.update"),
    path('reservation/delete/<int:id>', deleteReservation, name="reservation.delete"),
    path('order', OrderList.as_view(), name="order"),
    path('order/create', CreateOrder.as_view(), name="create.order"),
    path('order/update/<pk>', OrderUpdate.as_view(), name= "order.update"),
    path('menu', MenuList.as_view(), name="menu"),
    path('menu/<pk>/details', MenuDetails.as_view(), name="menu.details"),
    path('menu/delete/<int:id>', deleteMenu, name="menu.delete"),
    path('menu/create', CreateMenu.as_view(), name="create.menu"),
    path('menu/update/<pk>', MenuUpdate.as_view(), name= "menu.update"),
    path('ordermenu', OrderMenuList.as_view(), name="ordermenu"),
    path('ordermenu/create', CreateOrderMenu.as_view(), name="create.ordermenu"),
    path('ordermenu/update/<pk>', OrderMenuUpdate.as_view(), name= "ordermenu.update"),
    path('payment', PaymentList.as_view(), name="payment"),
    path('payment', viewPayment, name='payment'),
    path('payment/<pk>/details', PaymentDetails.as_view(), name="payment.details"),
    path('payment/create', CreatePayment.as_view(), name="create.payment"),
    path('payment/update/<pk>', PaymentUpdate.as_view(), name= "payment.update"),
    
    path('delivery', DeliveryList.as_view(), name="delivery"),
    path('delivery/create', CreateDelivery.as_view(), name="create.delivery"),
    path('delivery/update/<pk>', DeliveryUpdate.as_view(), name= "delivery.update"),
    path('orderdelivery', OrderDeliveryList.as_view(), name="orderdelivery"),
    path('orderdelivery/create', CreateOrderDelivery.as_view(), name="create.orderdelivery"),
    path('orderdelivery/update/<pk>', OrderDeliveryUpdate.as_view(), name= "orderdelivery.update"),
    path('reviews', ReviewsList.as_view(), name="review"),
    path('reviews', viewReview, name='reviews'),
    path('reviews/<pk>/details', ReviewDetails.as_view(), name="review.details"),
    path('reviews/create', CreateReviews.as_view(), name="create.reviews"),
    path('reviews/update/<pk>', ReviewsUpdate.as_view(), name= "reviews.update"),
    path('reviews/delete/<int:id>', deleteReview, name="review.delete")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



