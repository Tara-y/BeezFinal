from django import forms
from .models import User,Review

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'text']
