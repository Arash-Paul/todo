from django import forms
from .models import UserModel


class UserForm(forms.ModelForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        return email

    def clean_password(self):
        password = self.cleaned_data['passwor']
        return password

    class Meta:
        model = UserModel
        fields = '__all__'
