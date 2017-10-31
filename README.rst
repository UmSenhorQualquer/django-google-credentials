Django Google Credentials
=========================

Stores Google OAuth credentials in Django ORM for easy API service access.

Installation:
-------------
#. Install or add ``django-google-credentials`` to your Python path.

#. Add ``google_credentials`` to your ``INSTALLED_APPS`` setting.

#. Add ``google_credentials`` URL include to your project's ``urls.py`` file::
    
    url(r'^google-credentials/', include('google_credentials.urls')),

#. Create your project on the `Google API Console <https://code.google.com/apis/console>`_, specifying the redirect URL as ``http://your.domain.com/google-credentials/callback`` (or however you setup your ``urls.py`` as described above).

#. Add the following settings to your project's ``settings.py`` file populated with values as retrieved from Google in the previous step, i.e.::
   
    GA_CLIENT_ID = '32749234234.apps.googleusercontent.com'
    GA_CLIENT_SECRET = 'DKSFY87sd6fHJGdsf6'
    GA_SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'
    GA_REDIRECT_URI = 'http://your.domain.com/google-credentials/callback'

#. Run ``syncdb`` to generate required models.

Usage
-----
    
Before you can start using a service you have to authorize it with your Google account. To do this open `http://your.domain.com/google-credentials/authorize <http://your.domain.com/google-credentials/authorize>`_ in your browser. 

Once authorized you can retrieve a service for further querying like so::
	
	import httplib2
	from django.conf import settings
	from apiclient.discovery import build
	from google_credentials.models import Credentials
	from oauth2client.contrib.django_util.storage import DjangoORMStorage

	storage = DjangoORMStorage(Credentials, 'client_id', settings.GA_CLIENT_ID, 'credentials')
	credentials = storage.get()
	http = credentials.authorize(httplib2.Http())

	service	= build(serviceName='people', version='v1', http=http)

To purge previously generated credentials open `http://your.domain.com/google-credentials/purge <http://your.domain.com/google-credentials/purge>`_ in your browser.

