from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('story/<slug:slug>/', views.post_detail, name='post_detail'),
]