from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Staff(models.Model):
    number= models.IntegerField()
    gender=models.CharField(max_length=100)
    salary=models.IntegerField()
    address=models.CharField(max_length=100)
    department=models.TextField(null=False ,blank=False)
    working_hours=models.IntegerField()

class Category(models.Model):
    name=models.CharField(max_length=100)

class Reservation(models.Model):
    table_number=models.IntegerField()
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    number_of_people=models.IntegerField()
    RESERVATION_STATUSES = (
        ('Expired', 'Expired'),
        ('Active', 'Active'),
        ('Complete', 'Complete')
    )
    status=models.CharField(max_length=100, choices=RESERVATION_STATUSES)

class Order(models.Model):
    ORDER_STATUSES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )
    status=models.CharField(max_length=100, choices=ORDER_STATUSES)
    cost=models.IntegerField()
    is_delivery=models.BooleanField()
    order_number=models.IntegerField()
    staff_id=models.ForeignKey(Staff, on_delete=models.CASCADE)

    
class Menu(models.Model):
    MENU_TYPES=(
        ('Food', 'Food'),
        ('Drinks', 'Drinks')
    
    )
    type=models.CharField(max_length=100, choices=MENU_TYPES)
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    item=models.CharField(max_length=100)
    quantity=models.IntegerField()

class OrderMenu(models,Model):
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_id=models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity=models.IntegerField()

class Payments(models.Model):
    PAYMENT_STATUSES=(
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )
    status=models.CharField(max_length=100, choices=PAYMENT_STATUSES)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE)
    PAYMENT_MODES=(
        ('Mpesa', 'Mpesa'),
        ('Cash', 'Cash'),
        ('Card', 'Card')
    )
    payment_mode=models.CharField(max_length=100, choices=PAYMENT_MODES)

class Delivery(models.Model):
    DELIVERY_LOCATION_GROUPS=(
        ('CBD', 'CBD'),
        ('Within Nairobi', 'Within Nairobi'),
        ('Outside Nairobi', 'Outside Nairobi')
    )
    location_groups=models.CharField(max_length=100, choices=DELIVERY_LOCATION_GROUPS)
    delivery_fee=models.IntegerField()

class OrderDelivery(models.Model):
    customer_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE)
    location=models.CharField(max_length=100)
    ORDER_DELIVERY_STATUSES=(
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Enroute', 'Enroute')
    )
    status=models.CharField(max_length=100, choices=ORDER_DELIVERY_STATUSES)
    delivery_id=models.ForeignKey(Delivery, on_delete=models.CASCADE)

class Reviews(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    message=models.TextField()
    stars=models.IntegerField()






