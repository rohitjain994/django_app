from django.urls import path
from django.conf.urls import url, include
# from .views import SignUpView
from accounts import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', views.signup ,name='signup'),
    path('about/', views.about ,name='about'),
    path('profile/', views.profile ,name='profile'),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
     # Resete Password Urls
    # path('password-reset/', auth_views.PasswordResetView.as_view(
    #     template_name='registration/password_reset.html'), name='password_reset'),
    # path('password-reset/', auth_views.PasswordResetView.as_view(
    #     template_name='registration/password_reset.html'), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
    #     template_name='registration/password_reset_done.html'), name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    #     template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
    #     template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    # # Change Password Urls
    path('password_change/', auth_views.PasswordChangeView.as_view(
         template_name='registration/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
         template_name='registration/password_change_done.html'), name='password_change_done'),
]