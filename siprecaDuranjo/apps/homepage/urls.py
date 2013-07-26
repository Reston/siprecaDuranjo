from django.conf.urls import patterns, url

urlpatterns = patterns(
	'siprecaDuranjo.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^about/$', 'about', name="homepageabout"),
	url(r'^obras/$', 'obras', name="homepageobras"),
	url(r'^contacto/$', 'contact', name="homapagecontact"),
)
