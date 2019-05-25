from django import forms
from django.core.exceptions import ValidationError
from . import models
from .models import User


def UniqueUsernameIgnoreCaseValidator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this Username already exists.')


def UniqueEmailIgnoreCaseValidator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('This email is already used')


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'avatar']
        fields = ['username', 'password', 'email']
        # exclude = ['groups', 'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined',
        #            'name', 'last_name', 'first_name']
        labels = {
            'username': 'نام نمایشی',
            'password': 'رمز عبور',
            'email': 'ایمیل',

        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # super(SignUpForm, self).__init__()
        self.fields['username'].validators.append(UniqueUsernameIgnoreCaseValidator)
        self.fields['email'].validators.append(UniqueEmailIgnoreCaseValidator)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    # def is_valid(self):
    #     user = User.objects.first(username=self.username)
    #     if user is not None:
    #         return True
    #     else:
    #         return False

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'نام نمایشی',
            'password': 'رمز عبور',
        }
