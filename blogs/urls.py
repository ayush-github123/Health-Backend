from django.urls import path, include
from blogs import views


urlpatterns = [
    path('posts/', views.BlogListView.as_view(), name='post-list'),
    path('create-post/', views.BlogCreateView.as_view(), name='create-post'),
    path('posts/<int:pk>/', views.BlogDetailView.as_view(), name='post-detail'),

]
