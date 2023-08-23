from django.urls import path

from cats.views import index

urlpatterns = [
    path('', index)
]