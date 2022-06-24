from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Staff(User):
    staff_number= models.IntegerField(null=True, blank=True)
    GENDER_TYPES=(
        ('Male','Male'),
        ('Female', 'Female'),
        ('Other', 'Other')

    )
    gender=models.CharField(max_length=100, choices=GENDER_TYPES)
    salary=models.IntegerField(null=True, blank=True)
    address=models.CharField(max_length=100)
    DEPARTMENT_TYPES=(
        ('Waiter', 'Waiter'),
        ('Chef', 'Chef'),
        ('Admin', 'Admin')
    )
    department=models.CharField(max_length=200, choices=DEPARTMENT_TYPES)
    working_hours=models.IntegerField(default=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    table_number=models.IntegerField(blank=False)
    is_taken=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.table_number)

class Reservation(models.Model):
    table=models.ForeignKey(Table, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    people=models.IntegerField(default=True)
    RESERVATION_STATUSES = (
        ('Expired', 'Expired'),
        ('Active', 'Active'),
        ('Complete', 'Complete')
    )
    status=models.CharField(max_length=100, default="Active", choices=RESERVATION_STATUSES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.user.username + ' Table: '+ self.table

class Order(models.Model):
    ORDER_STATUSES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )
    status=models.CharField(max_length=100, default="Pending", choices=ORDER_STATUSES)
    cost=models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
    is_delivery=models.BooleanField(default=False)
    order_number=models.IntegerField(blank=True)
    staff=models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True, related_name="staff")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Menu(models.Model):

    FOOD = 'Food'
    DRINKS = 'Drinks'
    MENU_TYPES=(
        (FOOD, 'Food'),
        (DRINKS, 'Drinks')
    
    )
    type=models.CharField(max_length=100, choices=MENU_TYPES)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    item=models.CharField(max_length=100)
    price=models.FloatField(default=0.0)
    quantity=models.IntegerField()
    image=models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderMenu(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    menu=models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Payments(models.Model):
    PAYMENT_STATUSES=(
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )
    status=models.CharField(max_length=100, default="Pending", choices=PAYMENT_STATUSES)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    PAYMENT_MODES=(
        ('Mpesa', 'Mpesa'),
        ('Cash', 'Cash'),
        ('Card', 'Card')
    )
    payment_mode=models.CharField(max_length=100, default='Cash', choices=PAYMENT_MODES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Delivery(models.Model):
    DELIVERY_LOCATION_GROUPS=(
        ('CBD', 'CBD'),
        ('Within Nairobi', 'Within Nairobi'),
        ('Outside Nairobi', 'Outside Nairobi')
    )
    location_groups=models.CharField(max_length=100, choices=DELIVERY_LOCATION_GROUPS)
    delivery_fee=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderDelivery(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    location=models.CharField(max_length=100)
    ORDER_DELIVERY_STATUSES=(
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Enroute', 'Enroute')
    )
    status=models.CharField(max_length=100, default="Pending", choices=ORDER_DELIVERY_STATUSES)
    delivery_id=models.ForeignKey(Delivery, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reviews(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    message=models.TextField(null=True, blank=True)
    stars=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






