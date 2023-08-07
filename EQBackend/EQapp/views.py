from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import requests

from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpRequest


def signup(request):
    return HttpResponseRedirect('/djoser/users')


def get_token(request):
    return HttpResponseRedirect('/djoser/jwt/create')


@csrf_exempt
def combined_register(request):
    # signup(request)

    raw_data = dict()
    raw_data['email'] = request.POST.get('email')
    raw_data['password'] = request.POST.get('password')
    r = requests.post('/djoser/jwt/create', json=raw_data)

    token = get_token(r)
    return token
