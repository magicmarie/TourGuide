# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from tourapp.forms import TourismForm


def welcome(request):
    "Renders the landing page"
    form = TourismForm()

    context = {
        'form': form,
    }
    return render(request, 'welcome.html', context)

def tourist_home(request):
    "Renders the tourist home page"
    return render(request, 'tourist_home.html')

# def service_provider_home(request):
#     "Renders the login page"
#     return render(request, 'service_provider_home.html')
