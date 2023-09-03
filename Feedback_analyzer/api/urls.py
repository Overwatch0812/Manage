from django.urls import path
from .views import *

urlpatterns=[
    path('',studentApi.as_view())
]