from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACcf3690d72d99680a8f8edd027e6546fe"
# Your Auth Token from twilio.com/console
auth_token = "9f0876b6f50cd11876adcac9e19b412b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18584723940",
    from_="+18573824472",
    body="Hello from Python!")

print(message.sid)
