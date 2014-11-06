from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings	
from django.conf.urls.static import static 

urlpatterns = patterns('',
    # Examples:
     #url(r'^$', 'MiBrow.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
#	url(r'^$', views.index, name='index'),
	url(r'^search/', include('searchpage.urls')),
#k	url(r'test/', include('searchpage.urls')),
)	+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

