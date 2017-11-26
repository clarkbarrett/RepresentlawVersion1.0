# from django.urls import reverse
from django.shortcuts import render, HttpResponse, redirect
from myaccount.forms import (
    RegistrationForm,
    EditProfileForm,
)
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


""""# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Clark Barrett'

    args = {'username': name, 'numbers': numbers}
    return render(request, 'website/home.html', args)
    # return HttpResponse('Home Page')"""


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/website')
    else:
        # form = UserCreationForm()
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'myaccount/reg_form.html', args)


# @login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'myaccount/profile.html', args)


# @login_required
def edit_profile(request):
    if request.method == 'POST':
        # form = UserChangeForm(request.POST, instance=request.user)
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/myaccount/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'myaccount/edit_profile.html', args)


# @login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/myaccount/profile')
        else:
            return redirect('/myaccount/change_password.html')
        # TODO Limit login attempts

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'myaccount/change_password.html', args)
