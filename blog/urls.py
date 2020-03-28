from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('post-create/', views.post_create, name='post_create'),
    path('<slug:slug>/', views.post_details, name='post_details'),
    path('<slug:slug>/post-edit/', views.post_edit, name='post_edit'),
    path('<slug:slug>/post-delete/', views.post_delete),
]
