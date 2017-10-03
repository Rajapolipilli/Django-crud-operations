from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='ihome'),
    url(r'^create$', views.org_create, name='create'),
    url(r'^detail/(?P<id>\d+)/$', views.org_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.org_update, name='update'),
    url(r'^(?P<id>\d+)/delete$', views.org_delete, name='delete'),
    url( r'^employeedetail/(?P<id>\d+)/$', views.emp_detail, name='edetail' ),
    url(r'^empadd/$', views.emp_create, name='eadd'),
    url(r'^(?P<id>\d+)/modify/$', views.emp_update, name='eupdate'),
    url(r'^(?P<id>\d+)/remove/$', views.emp_delete, name='edelete'),

]