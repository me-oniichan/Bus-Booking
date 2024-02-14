from django import forms

from bus_auth.utils import password_validation, username_validation

class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, required=True, validators=[username_validation])
    password = forms.CharField(max_length=64, widget=forms.PasswordInput, required=True, validators=[password_validation])
    
    username.widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
    password.widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

class SingupForm(forms.Form):
    username = forms.CharField(max_length=64, required=True, validators=[username_validation])
    password = forms.CharField(max_length=64, widget=forms.PasswordInput, required=True, validators=[password_validation])
    email = forms.EmailField(max_length=64, required=True)

    username.widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
    password.widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
    email.widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
