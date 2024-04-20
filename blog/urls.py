from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detailed, name='post_detail'),
]