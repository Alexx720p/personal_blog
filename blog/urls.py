from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_article, name='add_article'),
    path('articles/<int:pk>/edit/', views.edit_article, name='edit_article'),
    path('delete/<int:pk>/', views.delete_article, name='delete_article'),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', auth_views.LoginView.as_view(), name='logout'),

]
