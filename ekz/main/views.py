from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .forms import CreateForm
from .models import Product


def index(request):
    rec = Product.objects.all()
    return render(request, 'main/index.html', {'rec': rec})


class LoginView(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('profile')


class LogoutView(LogoutView):
    template_name = 'main/logout.html'


# @login_required
# def profile(request):
#     return render(request, 'main/profile.html')


def info(request):
    return render(request, 'main/info.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def product(request):
    return render(request, 'main/product.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        form.save()
        return redirect('main:index')
    else:
        form = CreateForm
    context = {'form': form}
    return render(request, 'main/profile.html', context)