from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=150, label='Nome Completo', required=True)

    class Meta:
        model = CustomUser
        fields = ("full_name", "username", "email")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("full_name", "username", "email")
