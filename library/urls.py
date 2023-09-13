from django.urls import path
from . import views

urlpatterns = [
    path('Books_Library/', views.Books_Library_View, name='Books_Library')
]