#Here is were I am going to put the sart page urs.
from django.conf.urls import url

from searchpage import views

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^test/', views.result, name='test'),

]
 
