from django.conf.urls import patterns, url

from char_sheet import views

urlpatterns = patterns('',
    url(r'^$', views.userView, name='index'),
    url(r'^createCharacter/', views.createCharacter, name="createCharacter"),
    url(r'^deleteCharacter/(\d+)$', views.deleteCharacter, name="deleteCharacter"),
    url(r'^displayCharacter/(\d+)$', views.displayCharacter, name="displayCharacter"),
   url(r"^user/", views.userView, name="user")
    )

