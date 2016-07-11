from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
]