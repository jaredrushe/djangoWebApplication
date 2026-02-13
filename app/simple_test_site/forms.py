from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': _('Username'),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        # Allow spaces in usernames
        return username.strip()  # Strip any leading or trailing spaces

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the 'validators' attribute to allow spaces in usernames
        self.fields['username'].validators = []