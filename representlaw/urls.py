"""representlaw path Configuration

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path(r'^$', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.conf.paths import path, include
    2. Add a path to pathpatterns:  path(r'^blog/', include('blog.paths'))
"""
# from django.urls import include, path
from representlaw import views as representlaw_views


from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [

    url(r'^', include('website.urls', namespace='website')),
    url(r'^admin/', admin.site.urls),
    url(r'^myaccount/', include('myaccount.urls', namespace='myaccount')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^contact/', include('sendemail.urls', namespace='sendemail')),
    # url(r'^contact/$', ContactView.as_view(), name='envelope-contact'),
    # url(r'^contact/', include('sendemail.urls', namespace='sendemail')),
    # url(r'^website/', include('website.urls', namespace='website')),
]
