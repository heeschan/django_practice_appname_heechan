from django.http import HttpResponse ##vscode에서도 전구 눌러서 지원
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return HttpResponse('Hello world! 안녕하세요?')