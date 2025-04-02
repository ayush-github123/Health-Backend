from django.urls import path, include
from blogs import views


urlpatterns = [
    path('posts/', views.BlogListCreateView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.BlogDetailView.as_view(), name='post-detail'),

]
