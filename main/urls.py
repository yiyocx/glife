from django.conf.urls import url

from main import views

urlpatterns = [
    url(r'^users/$', views.ListUsers.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='user-detail'),
]