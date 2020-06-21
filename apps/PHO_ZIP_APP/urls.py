from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^phozipmenu$', views.phozipmenu),
    url(r'^phochamenu$', views.phocahmenu),
    url(r"^drinkmenu$", views.drinkmenu),
    url(r'^contact$', views.contact),
]