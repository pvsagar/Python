# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:41:50 2018

@author: VidyaSagar
"""

from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "ACd7875ab9254a2b737c1103382c7d2d7c"
# Your Auth Token from twilio.com/console
auth_token = "1c722157fbe91d652acac32fc87060b9"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(
    to="+12013817554",
    from_="++16157634107",
    body="Hello from Python!")

print(message.sid)
