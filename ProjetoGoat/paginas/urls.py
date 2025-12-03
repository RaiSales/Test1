from django.urls import path
from .views import P1

urlpatterns = [
        path('',P1.as_view(), name='/p1')
    ]