from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^job_posts',views.job_post,name="job_post"),
    url(r'^dashboard',views.dashboard,name="dashboard"),
    url(r'^job_post_details/(?P<status>(\d+))/$',views.job_post_details,name="job_post_details"),
    url(r'^submit',views.Send_jobpost,name="Send_jobpost"),
    url(r'^specific_post/(?P<id>(\d+))/',views.specific_post,name="specific_post"),
    url('',views.signin,name="signin")
    ]

