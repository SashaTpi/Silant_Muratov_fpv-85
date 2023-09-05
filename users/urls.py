from django.urls import path
from users import views

urlpatterns = [
    path('api/user', views.user, name='user'),
    path('api/login', views.issue_token, name='issue_token'),
]