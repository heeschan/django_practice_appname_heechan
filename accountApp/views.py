from django.http import HttpResponse ##vscode에서도 전구 눌러서 지원
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'base.html') #8강