from django import forms
from .models import CustomUserProfile

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = ['email', 'first_name', 'last_name', 'bio', 'avatar', 'password']


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)