from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


def signup(request):
    return HttpResponseRedirect('/djoser/users')


def get_token(request):
    return HttpResponseRedirect('/djoser/jwt/create')


def combined_register(request):
    signup(request)
    token = get_token(request)
    return token
