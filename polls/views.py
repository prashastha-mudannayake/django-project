# -*- coding: utf-8 -*-
from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><head></head><body><h1>Hello, world. You're at the polls index.</h1></body></html>")


def page(request):
    return HttpResponse("<html><head></head><body><h1>Hello, world. You're at the polls page.</h1></body></html>")
