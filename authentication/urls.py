from django.urls import path
from .views import Register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout')
]