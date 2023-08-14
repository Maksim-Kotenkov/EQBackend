import requests
import json
import yaml
from yaml.loader import SafeLoader

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse, HttpRequest
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from EQBackend.settings import address
from .models import Tests
from .serializers import UserProfileSerializer, AnswerSerializer


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
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if request.method == 'GET':
            test = Tests.objects.filter(pk=kwargs['pk'])[0]
            r = dict()
            r['name'] = test.name
            r['type'] = test.type
            yml = yaml.load(test.test_data, Loader=SafeLoader)
            r['test_data'] = yml
            r['counting_function'] = test.counting_function

            return Response(r)

        elif request.method == 'POST':
            answer = json.loads(str(self.request.body, encoding='utf-8'))
            answer['answers'] = yaml.dump(answer['answers'])
            answer['user'] = request.user.pk
            serializer = AnswerSerializer(data=answer)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
