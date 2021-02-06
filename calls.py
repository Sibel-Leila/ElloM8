# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

#constants
account_sid = 'x'
auth_token = 'x'

client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+x',
                        from_='+x'
                    )

print(call.sid)
