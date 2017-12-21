from django.conf.urls import url
from google_credentials.views   import authorize, callback, purge

urlpatterns = [
    url(r'^authorize$', authorize),
    url(r'^callback$', callback),
    url(r'^purge$', purge),
]