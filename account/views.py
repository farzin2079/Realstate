from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

from django.contrib.auth.models import User
from .models import Profile
from property.models import Category
from .forms import ProfileForm


@login_required(login_url='/login')
def index(request):
    profile = Profile.objects.get(user=request.user)
    categorys = Category.objects.all()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "chenge seved")
        else:
            messages.error(request, "not valid dates")

        watchlist = profile.watchlist.all()
        prop = profile.propertys.all()
        return render(
            request,
            "account/index.html",
            {
                "profile": profile,
                "watchlist": watchlist,
                "propertys": prop,
                "imageField": ProfileForm,
                "categorys": categorys,
            },
        )
    else:
        profile = Profile.objects.get(user=request.user)
        watchlist = profile.watchlist.all()
        prop = profile.propertys.all()
        return render(
            request,
            "account/index.html",
            {
                "profile": profile,
                "watchlist": watchlist,
                "propertys": prop,
                "categorys": categorys,
                "imageField": ProfileForm,
            },
        )


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            messages.success(request, "login")
            return redirect("/")
        else:
            messages.error(request, "invalide username and/or password")
            return redirect("login")
    else:
        return render(request, "account/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "logout")
    return redirect("login")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            # Message
            messages.error(request, "password and confirmtion most be same")
            return redirect("register")
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.error(request, "username is already exist")
            return redirect("register")
        
        login(request, user)

        messages.success(request, "registre successfull")
        return HttpResponseRedirect(reverse("account"))
    else:
        return render(request, "account/register.html")


@login_required(login_url='/login')
def profile(request, id):
    user = User.objects.get(pk=id)
    profile = Profile.objects.get(user=user)
    prop = profile.propertys.all()
    categorys = Category.objects.all()

    return render(
        request,
        "account/profile.html",
        {"profile": profile, "propertys": prop, "categorys": categorys},
    )
