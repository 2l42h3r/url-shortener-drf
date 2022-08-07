from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten),
    path('<str:shortened>', views.redirect_url)
]
