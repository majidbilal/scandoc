from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    username = forms.CharField(label='User Name')
    password = forms.CharField(widget=forms.PasswordInput, label='Email Address')

    def clean_username(self):
        user = self.cleaned_data['username']
        if not User.objects.filter(username=user):
            raise forms.ValidationError("User doesn't Exist.")


