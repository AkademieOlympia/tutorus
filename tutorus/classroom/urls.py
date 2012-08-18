from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'^create/$', views.create_classroom, name='class_create'),
    url(r'^(?P<classroom_id>\w+)/$', views.class_create_step, name='class_create_step'),
    url(r'^(?P<classroom_id>\w+)/activate/$', views.class_activate, name='class_activate'),
    url(r'^(?P<classroom_id>\w+)/take/$', views.class_take, name='class_take'),
    url(r'^$', views.home, name='class_home'),
)