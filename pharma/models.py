from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10,null=False)
    def __str__(self):
        return f"{self.user.username} - {self.address} - {self.mobile}"

#create model of register online boy
class Delivery_boy(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10,null=False)
    vechile=models.CharField(max_length=13,null=False)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} - {self.vechile} - {self.mobile}"

#product
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=3) 

    profile = models.ImageField(upload_to='product_pic/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - ${self.price}"  # This will display both the name and price


#create model of payment details with card
class Payment(models.Model):
    card_number = models.CharField(max_length=19)  
    expiration_date = models.CharField(max_length=5)  
    cv_code = models.CharField(max_length=3)  
    card_owner = models.CharField(max_length=100)

#create model of feedback 
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True) 
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

#model of order and delivery


class Address(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')  # Link to the User model
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    shipping_address = models.TextField()
    phone_number = models.CharField(max_length=10)
    products = models.ManyToManyField('Products',related_name='bookings',blank=True)  # Can be null for existing rows
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    date = models.DateTimeField(default=datetime.now) 
    tracking_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Order by {self.full_name} on {self.date}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, blank=True)
    

