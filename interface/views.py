#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse


def home(request):

    return render(request, 'interface/accueil.html', locals())
