from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_data),
    url(r'^save/$',views.save_data),
]
    
