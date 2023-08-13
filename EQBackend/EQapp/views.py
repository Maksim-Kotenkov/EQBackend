from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import requests
import json
import yaml

from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from rest_framework import viewsets

from EQBackend.settings import address
from .models import Tests


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


class TestView(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.request.method == 'GET':
            test = Tests.objects.filter(pk=self.kwargs['pk'])[0]
            r = dict()
            r['name'] = test.name
            r['type'] = test.type
            yml = dict()
            yaml.load(test.test_data, yml)
            r['test_data'] = yml
            r['counting_function'] = test.counting_function
            return HttpResponse(r)

        elif self.request.method == 'POST':
            test = Tests.objects.filter(pk=self.kwargs['pk'])
            return test
        else:
            bad_resp = HttpResponse()
            bad_resp.text = 'Method not allowed.'
            return bad_resp
