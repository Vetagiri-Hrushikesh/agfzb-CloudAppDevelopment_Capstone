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

logger = logging.getLogger(__name__)

def static_template_view(request):
    return render(request, 'djangoapp/static_template.html')

def about_template_view(request):
    return render(request, 'djangoapp/about.html')


def contact_template_view(request):
    return render(request, 'djangoapp/contact.html')

def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)