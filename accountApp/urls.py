from django.urls import path
from accountApp.views import hello_world

app_name = 'accountApp' ##추후 나올 함수로 라우트 주소 간단화

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]