from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import requests
import json

from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from EQBackend.settings import address


@csrf_exempt
def signup(request):
    r = requests.post(url=f'{address}/djoser/users/', json=json.loads(request.body))

    if r.status_code == 200:
        token = get_token(request)
        return token
    else:
        bad_resp = HttpResponse()
        bad_resp.status_code = r.status_code
        bad_resp.text = r.text
        return bad_resp


@csrf_exempt
def get_token(request):
    raw_data = dict()
    json_data = json.loads(request.body)
    print(json_data)
    raw_data['email'] = json_data['email']
    raw_data['password'] = json_data['password']
    r = requests.post(url=f'{address}/djoser/jwt/create', json=raw_data)

    return HttpResponse(r)
