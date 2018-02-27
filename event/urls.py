"""Ticketr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import event.views

urlpatterns = [
    url(r'^$', event.views.Home.as_view(), name='index'),
    url(r'^create/', event.views.CreateEvent.as_view(), name='create-event'),
    url(r'^manage/', event.views.ManageEvents.as_view(), name='manage-events'),
    url(r'^organisers-profile/(?P<organiser_id>[0-9]+)$', event.views.OrganisersProfile.as_view(),
        name='organisers-profile'),
    url(r'(?P<event_id>[0-9]+)$', event.views.ViewEvent.as_view(), name='view-event'),
    url(r'^browse/',event.views.ListEvents.as_view(), name='browse-events'),
    url(r'^organiser-profiles/',event.views.OrganiserProfiles.as_view(), name='organiser-profiles')
]
