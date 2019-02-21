from django import forms
from django.contrib.auth.models import User

from userprofiles.models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Email address')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']


