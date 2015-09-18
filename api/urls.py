from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

from api import views

urlpatterns = [
    url(r'^users/$', views.ListUsers.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='user-detail'),
    url(r'^api-token-auth/', obtain_auth_token),
]