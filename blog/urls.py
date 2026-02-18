from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.posts, name='post_list'),
    path('category/<slug:category_slug>/', views.posts, name='post_category_list'),
    path('post/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('tag/<slug:tag_slug>/', views.posts, name='post_list_by_tag')
]

