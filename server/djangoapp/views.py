from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return render(request, 'djangoapp/index.html',{})

# Create an `about` view to render a static about page
def about(request):
    return render(request, 'djangoapp/about.html',{})


# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'djangoapp/contact_us.html',{})
# Create a `login_request` view to handle sign in request
def login_request(request):
        context = {}
        # Handles POST request
        if request.method == "POST":
            # Get username and password from request.POST dictionary
            username = request.POST['username']
            password = request.POST['psw']
            # Try to check if provide credential can be authenticated
            user = authenticate(username=username, password=password)
            if user is not None:
                # If user is valid, call login method to login current user
                login(request, user)
        return redirect('djangoapp:about')
             

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    return redirect('djangoapp:about')

# Create a `registration_request` view to handle sign up request
def registration_request(request):

    return render(request, 'djangoapp/registration.html',{})
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

