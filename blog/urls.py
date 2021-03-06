from . import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .feeds import RSSSiteNewsFeed, AtomSiteNewsFeed


app_name = "blog"

urlpatterns = [
    url(r'^$', views.list_of_post, name='list_of_post'),
    # url(r'^$', TemplateView.as_view(template_name='blog/list_of_post.html'), name='list_of_post'),
    url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.list_of_post_by_category, name='list_of_post_by_category'),
    url(r'^(?P<slug>[-\w]+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^rss/feed/$', RSSSiteNewsFeed()),
    url(r'^sitenews/atom/$', AtomSiteNewsFeed()),
]

# TODO haystack search

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)