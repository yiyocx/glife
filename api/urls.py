from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token

from api import views

urlpatterns = [
	url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^users/$', views.UserListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='user-detail'),
    url(r'^tags/$', views.TagListView.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetailView.as_view(), name='tag-detail'),
    url(r'^documents/(?P<pk>[0-9]+)/upvote/$', views.upvote_document),
    url(r'^documents/(?P<pk>[0-9]+)/downvote/$', views.downvote_document),
    url(r'^auth/', include('djoser.urls')),
    url(r'^api-token-auth/', obtain_auth_token),
]