from django import forms
from django.contrib.auth.models import User
from learningapp.models import UserDetails
from django_recaptcha.fields import ReCaptchaField
from foodsapp.models import FoodItems

class UserForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())
     class Meta:
        model = User
      #   fields = "__all__"
        fields = ['username','email','password']

class UserprofileForm(forms.ModelForm):
   class Meta:
      model = UserDetails
      fields =['phone','address','street','city','zipcode','userpic']
   captcha = ReCaptchaField()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileUpdateForm(forms.ModelForm):
   class Meta:
      model = UserDetails
      fields =['phone','address','street','city','zipcode','userpic']
      
      
class addFoodForm(forms.ModelForm):
    class Meta:
        model = FoodItems
        fields = ['name', 'price', 'rating', 'description', 'foodimg', 'catogery']
