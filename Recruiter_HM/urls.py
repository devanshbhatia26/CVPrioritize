from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^logout', views.logout_view, name="logout_view"),
    url(r'^dashboard',views.dashboard,name="dashboard"),
   
    url(r'^job_post_details$',views.job_post_details,name="job_post_details"),
    #url(r'^match',views.match,name="match"),
  
   
  
    url(r'^specific_post/(?P<id>(\d+))/',views.specific_post,name="specific_post"),
    url(r'^edit_jd/(?P<id>(\d+))/',views.edit_jd,name="edit_jd"),
    url(r'^publish_jd/(?P<id>(\d+))/',views.publish_jd,name="publish_jd"),
    url(r'^show_jd/(?P<id>(\d+))/',views.show_jd,name="show_jd"),
    
    url(r'^$',views.signin,name="signin"),
    url(r'^success_jd/(?P<id>(\d+))/',views.success_jd,name="success_jd"),
    url(r'^unsuccess_jd/(?P<id>(\d+))/',views.unsuccess_jd,name="unsuccess_jd"),

    url(r'^job_post$',views.job_post,name="job_post"),   
   
]   

