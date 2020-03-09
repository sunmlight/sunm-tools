from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("get_key", views.GetKey.as_view(), name="get_key"),
]