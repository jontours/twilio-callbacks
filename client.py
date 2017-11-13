# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC9e8889d7b29a7fa348c5d0fcb7e082ea"
auth_token = "6b516c15db1716a76e550f3870ccb3e1"
client = Client(account_sid, auth_token)
'''
message = client.api.account.messages.create(
    to="+18082246036",
    from_="+18086644992",
    body="Dopppty duuu another test!",
    url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient",
    media_url=['https://demo.twilio.com/owl.png',
               'https://demo.twilio.com/logo.png'])
'''

call = client.calls.create(to="+18082246036",
                           from_="+18086644992",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")