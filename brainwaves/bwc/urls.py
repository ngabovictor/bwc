from django.conf.urls import url
from . import views


urlpatterns = [
                url('^$', views.index),
                url('what-we-do', views.whatwedo),
                url('publications/$', views.publications),
                url('our-programs/$', views.ourprograms),
                url('trainings/$', views.trainings),
                url('all-programs', views.allprograms),
                url('all-trainings', views.alltrainings),
                url('contact/$', views.contact),
                url(r'join-program',views.joinprogram),
                url('register/$',views.register),
                url(r'send-message',views.sendmessage),
                url(r'registering',views.registering),
               ]
