# sendemail/urls.py
from django.contrib import admin
from django.conf.urls import include, url

from . import views

app_name = "sendemail"

urlpatterns = [
    # url('^email/', views.emailView, name='email'),
    url(r'^$', views.emailView, name='email'),
    # url('^success/', views.successView, name='success'),
    url('^contact/', views.successView, name='success'),
]

"""url(r'^conveyancing-commercial/$',
        TemplateView.as_view(template_name='website/conveyancing-commercial/conveyancing-commercial-home.html'),
        name='conveyancing-commercial-home'),"""