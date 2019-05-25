from django.urls import path
from . import views
from django.contrib.auth import login

urlpatterns = [
    path('', views.show_signup),
    path('signup', views.do_signup, name="submit_registration"),
    path('login', views.show_login, name = "login_page"),
    path('logout', views.user_logout),
    path('do_login', views.do_login, name="login"),
    # path('login', views.login_form),
    # path('auth', views.login, name="login")
]
