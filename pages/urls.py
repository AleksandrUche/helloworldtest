from django.urls import path

from pages.views import *

urlpatterns = [
    path('', homePageView, name='home'),
]
