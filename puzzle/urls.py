from django.urls import path
from . import views

urlpatterns = [
    path('', views.last_puzzle, name='last_puzzle'),
    path('pass_level', views.pass_level, name='pass_level'),
    # path('last_puzzle', views.last_puzzle, name = 'last_puzzle')
]
