from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token

from api import views

urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view(), name='rest_register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='rest_login'),
    url(r'^users/$', views.UserListCreateView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='user-detail'),
    url(r'^api-token-auth/', obtain_auth_token),
]