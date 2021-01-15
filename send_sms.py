# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC2854bff1bbfbbdb441498605145b3a93'
auth_token = 'a959f9fb939474f8354bbd0a922c131e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='MGe1a55d78a3e353da09f1a9871447cce3',
                     to='+16047004571'
                 )

print(message.sid)