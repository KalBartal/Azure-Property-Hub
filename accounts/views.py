# accounts/views.py

from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
