# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:41:50 2018

@author: VidyaSagar
"""

from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "Your account ID"
# Your Auth Token from twilio.com/console
auth_token = "Your auth token"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(
    to="Your phone Number",
    from_="Twillo phone",
    body="Hello from Python!")

print(message.sid)
