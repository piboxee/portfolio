from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_index'),
    path('<slug:post>', views.blog_category_list_view, name='category_index'),
    path('post-create/', views.post_create, name='post_create'),
    path('<str:category>/<slug:slug>/', views.post_details, name='post_details'),
    path('<slug:slug>/post-edit/', views.post_edit, name='post_edit'),
    path('<slug:slug>/post-delete/', views.post_delete),
]
