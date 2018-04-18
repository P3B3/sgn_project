from django.conf.urls import url
from django.urls import path, include
from home.views import HomeView
from . import views

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('connect/<operation>/<int:pk>/', views.change_friends, name='change_friend')
]
