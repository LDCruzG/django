from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('welcome/<str:nombre>/<str:apellido>/', views.welcome_view, name='welcome'),
]