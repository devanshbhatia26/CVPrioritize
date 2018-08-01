from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.index, name = "home"),
    url('<int:candidate_id>editdetails/', views.editdetails, name='editdetails'),
]
