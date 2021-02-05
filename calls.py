# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

#constants
account_sid = "x"
auth_token = "x"

client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+x',
                        from_='+x'
                    )

print(call.sid)

# class Call:
#     def __init__(self):
#         self.FROM = FROM
#         self.CALLED = CALLED
#         self.ACCOUNT_SID = ACCOUNT_SID
#         self.AUTH_TOKEN = AUTH_TOKEN
#         self.callCounter = 0 # how many calls we made and iterates with calls
#         self.LIMIT = 20 # limit of outgoing calls before exiting
#
#     def set_target(self):
#         self.CALLED = str(input("enter phoone number of target, use +1 bbefore: "))
#
#     def makeCall(self):
#         client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN)
#
#         while self.callCounter < self.LIMIT:
#             call = client.call.create(to = self.CALLED, from_ = self.FROM, url = "https://demo.twilio.com/docs/voice.xml") # https://demo.twilio.com/docs/voice.xml
#             self.callCounter = self.callCounter + 1
#             print("Call # " + str(self.callCounter) + " Callling number: " + str(self.CALLED))
#             time.sleeep(20)
#
# def main():
#     ElloM8 = Call()
#     ElloM8.makeCall()
#
# if __name__ == "__main__":
#     main()
