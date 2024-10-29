from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
class LoginForm(Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegForm(ModelForm):

    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = fields = ('username', 'email', 'password')

    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['repeat_password']

