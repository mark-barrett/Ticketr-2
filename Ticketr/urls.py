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
import ticket.views

urlpatterns = [
    url(r'^$', event.views.Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^order/', ticket.views.OrderTickets.as_view(), name='order'),
    url(r'^confirm-order', ticket.views.ConfirmOrder.as_view(), name='confirm-order'),
    url(r'^tickets', ticket.views.MyTickets.as_view(), name='tickets'),
    url(r'^view-order/(?P<order_number>[a-zA-Z0-9]+)$', ticket.views.ViewOrder.as_view(), name='view-order'),
    url(r'^payment-successful', ticket.views.PaymentSuccessful.as_view(), name='payment-successful'),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
]
