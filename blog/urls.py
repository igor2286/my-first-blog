from django.urls import path, include
from . import views
from .views import dashboard


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('accounts/', include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", views.register, name='register'),
]

