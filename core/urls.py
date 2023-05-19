from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('registro/', signup, name='registro'),
    path('contas/login/', MyLoginView.as_view(), name='login'),
    path('accounts/', include('allauth.urls')),
]