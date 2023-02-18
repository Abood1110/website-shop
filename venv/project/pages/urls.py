from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('register',views.register,name='register')
]
