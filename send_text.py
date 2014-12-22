from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC673a0d87c7d55037989e66f0c82c4b80"
auth_token  = "ba81162524d067a22570c04e11b2ae6b"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Do you want to eat a Wafle with me for lunch?",
    to="+19194555142",    # Replace with your phone number
    from_="+12602014107") # Replace with your Twilio number
print message.sid
