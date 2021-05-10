from django.urls import path
from django.conf.urls import url, include
# from .views import SignUpView
from accounts import views

urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', views.signup ,name='signup'),
    path('about/', views.about ,name='about'),
    path('profile/', views.profile ,name='profile'),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
]