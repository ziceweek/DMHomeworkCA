__author__ = 'zice'

from weibo import APIClient

APP_KEY = '2038546250'
APP_SECRET = '24bb05a6fb21eadf36713d75f2fe2b77'
CALLBACK_URL = 'http://www.example.com/callback'


code = '8067a19c36a182b6643d77825ccc3ab4'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in
print access_token
print expires_in

client.set_access_token(access_token, expires_in)
s = client.is_expires()
print s