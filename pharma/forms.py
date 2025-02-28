from django import forms
from django.contrib.auth.models import User
from.import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets={
            'password':forms.PasswordInput()
        }
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']        

#online delivery boy 
class DeliveryUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets={
            'password':forms.PasswordInput()
        }

class DeliveryForm(forms.ModelForm):
    class Meta:
        model=models.Delivery_boy
        fields=['address','mobile','profile_pic','vechile']     



#payment details with card
class PaymentForm(forms.ModelForm):
    class Meta:
        model =models.Payment
        fields = ['card_number', 'expiration_date', 'cv_code', 'card_owner']

#feedback form
class FeedbackForm(forms.ModelForm):
    class Meta:
        model =models.Feedback
        fields = ['name', 'email', 'feedback']

#address for chechkout
class AddressForm(forms.ModelForm):
    class Meta:
        model=models.Address
        fields=['full_name', 'email', 'shipping_address', 'phone_number']


class PrescriptionForm(forms.Form):
    file=forms.ImageField()
