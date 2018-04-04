from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path('', views.ItemView.as_view(), name='index'),
    path('item/<int:pk>/', views.ModifyItemView.as_view(), name='edit'),
    path('accounts/login/', auth_views.LoginView.as_view()),
]

