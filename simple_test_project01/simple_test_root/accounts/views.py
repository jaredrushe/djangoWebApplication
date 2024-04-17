from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AdminUserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse


class SignUpView(CreateView):
    form_class = AdminUserCreationForm  # Use custom form
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


