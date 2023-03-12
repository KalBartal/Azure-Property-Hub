from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Message



class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'regular'  # set role here
            user.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def index(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'New message from Azure Property Hub',
                f'From: {name} <{email}>\n\n{message}',
                email,
                ['admin@example.com'],
                fail_silently=False,
            )
            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


@login_required
def inbox(request):
    messages = Message.objects.filter(
        recipient=request.user).order_by('-created_at')
    return render(request, 'messaging/inbox.html', {'messages': messages})

def handler404(request, exception):
    response = render(request, '404.html')
    response.status_code = 404
    return response