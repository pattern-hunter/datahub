from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_data),
    url(r'^auth/',views.auth_view),
    url(r'^logout/',views.logout_view),
    url(r'^dashboard/',views.dashboard_view),
    url(r'^save/$',views.save_data),
]
    
