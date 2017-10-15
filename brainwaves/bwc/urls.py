from django.conf.urls import url
from . import views


urlpatterns = [
                url('^$', views.index),
                url('what-we-do', views.whatwedo),
                url('publications/$', views.publications),
                url('our-programs/$', views.ourprograms),
                url('our-programs/q=(?P<program_id>\d+)', views.ourprogram),
                url('trainings/$', views.trainings),
                url('trainings/q=(?P<training_id>\d+)', views.ourtraining),
                url('all-programs', views.allprograms),
                url('all-trainings', views.alltrainings),
                url('contact/$', views.contact),
                url(r'join-program&p=(?P<program_id>\d+)', views.joinprogram),
                url(r'join-program-in',views.joinprogram_in),
                url(r'register-program&t=(?P<training_id>\d+)',views.register),
                url(r'send-message',views.sendmessage),
                url(r'registering',views.registering),
               ]
