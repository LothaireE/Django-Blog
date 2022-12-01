

from django.urls import path, include
from .views import article_list, article_details, user_login, register, article_form, article_update, article_delete
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', article_list, name='article_list'),
    path('article/<slug:slug>/', article_details, name='article_details'),
    path('articles/add/', article_form, name='article_form'),
    path('update/<slug:slug>/', article_update, name='article_update'),
    path('delete/<slug:slug>/', article_delete, name='article_delete'),


    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', register, name='register'),

    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('social-auth/', include('social_django.urls', namespace='social'))
]