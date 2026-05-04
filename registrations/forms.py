from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(label='Please enter your first name:', widget= forms.TextInput(attrs={'placeholder':'First Name','maxlength': '50',}))
    last_name = forms.CharField(label='Please enter your last name:', widget= forms.TextInput(attrs={'placeholder': 'Last Name','maxlength': '50',}))
    company_ID = forms.CharField(label= 'Please enter your Company ID:', widget=forms.TextInput(attrs={'placeholder': 'Company ID', 'maxlength': '7', 'minlength': '7'}))
    username = forms.CharField(label='Please enter your Company CDSID', widget=forms.TextInput(attrs={'placeholder':'Company CDSID','maxlength': '20',}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'company_ID', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Please enter your Company CDSID:', widget=forms.TextInput(attrs={'placeholder':'Company CDSID'}))
    password = forms.CharField(label='Please enter your password:', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

