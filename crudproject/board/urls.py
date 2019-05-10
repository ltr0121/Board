from board import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('post/', views.post, name='post'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('show/', views.show, name='show'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]