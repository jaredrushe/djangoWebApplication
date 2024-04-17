from django import forms
from django.contrib.auth.forms import UserCreationForm

class AdminUserCreationForm(UserCreationForm):
    admin_password = forms.CharField(
        label='Admin Password', 
        widget=forms.PasswordInput, 
        required=False,
        help_text="Only necessary to create a staff account."
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('admin_password',)

    def clean_admin_password(self):
        admin_password = self.cleaned_data.get('admin_password')
        if admin_password and admin_password != "toonarmy":
            raise forms.ValidationError("Invalid admin password")
        return admin_password

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('admin_password') == "toonarmy":
            user.is_staff = True
        if commit:
            user.save()
        return user



