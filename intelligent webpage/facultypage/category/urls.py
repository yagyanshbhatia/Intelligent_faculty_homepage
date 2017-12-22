from django.conf.urls import url
from . import views

app_name = 'category'

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^email/$', views.email, name='email'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^home/$', views.home, name='home'),
    url(r'^publications/$', views.publications, name='publications'),
    url(r'^deleteteaching/(?P<pk>[0-9]+)/$', views.deleteteaching, name='deleteteaching'),
    url(r'^deleteedu/(?P<pk>[0-9]+)/$', views.deleteedu, name='deleteedu'),
    url(r'^deleteexperience/(?P<pk>[0-9]+)/$', views.deleteexperience, name='deleteexperience'),
    # url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    # url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
     url(r'^createabout/$', views.createabout, name='createabout'),
    url(r'^editabout/$', views.editabout, name='editabout'),
    url(r'^aboutto/(?P<user_name>.*)/$',views.aboutto,name='aboutto'),
    url(r'^todolist/$', views.todolist, name='todolist'),
    url(r'^createeducation/$', views.createeducation, name='createeducation'),
    url(r'^education/$', views.education, name='education'),
    url(r'^teaching/$', views.teaching, name='teaching'),
    url(r'^addteaching',views.addteaching,name="addteaching"),
    url(r'^createexperience/$', views.createexperience, name='createeducation'),
    url(r'^createtodo/$', views.createtodo, name='createtodo'),
    url(r'^experience/$', views.experience, name='education'),
    url(r'^deletetodo/(?P<pk>[0-9]+)/$', views.deletetodo, name='deletetodo'),
    # url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    # url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    # url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    # url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]