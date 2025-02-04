from django.urls import path
from .views import user_login, register, user_status


urlpatterns=[
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('user_status/', user_status, name='user_status')

]
