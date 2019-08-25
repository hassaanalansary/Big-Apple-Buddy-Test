from django.conf.urls import url
from job_app import views

app_name = 'job_app'
urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^view1/$', views.view1, name='view1'),
    url(r'^view2/$', views.view2, name='view2'),
]
