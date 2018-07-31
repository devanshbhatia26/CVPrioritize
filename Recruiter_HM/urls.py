from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^job_posts',views.job_post,name="job_post"),
    url(r'^dashboard',views.dashboard,name="dashboard"),
    url('',views.signin,name="signin")
    ]

