from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^job_posts',views.job_post,name="job_post"),
    url(r'^dashboard',views.dashboard,name="dashboard"),
    url(r'^job_post_details',views.job_post_details,name="job_post_details"),
    url(r'^submit',views.Send_jobpost,name="Send_jobpost"),
    url(r'^specific_post/(?P<id>(\d+))/',views.specific_post,name="specific_post"),
    url(r'^edit_jd/(?P<id>(\d+))/',views.edit_jd,name="edit_jd"),
    url(r'^publish_jd/(?P<id>(\d+))/',views.publish_jd,name="publish_jd"),
    url(r'^review_jd/(?P<id>(\d+))/',views.review_jd,name="review_jd"),
    url('',views.signin,name="signin")
    ]

