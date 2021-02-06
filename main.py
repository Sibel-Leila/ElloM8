from twilio.rest import Client
from jokeapi import Jokes

# constants
account_sid = ''
auth_token = ''
to_call = ''
from_call = ''

j = Jokes()  # Initialise the class
joke = j.get_joke(lang='en',
                category=['misc', 'pun', 'spooky', 'christmas'],
                blacklist=['nsfw', 'religious', 'political', 'racist', 'sexist']) # Retrieve a random joke

client = Client(account_sid, auth_token)

if joke['type'] == 'single': # Print the joke
    print(joke['joke'])
    response = '<Response><Say>' + joke['joke'] + '</Say></Response>'
else:
    print(joke['setup'])
    print(joke['delivery'])
    response = '<Response><Say>' + joke['setup'] +  '</Say><Pause length="5"/><Say>' + joke['delivery'] + '</Say></Response>'

call = client.calls.create(
                        twiml=response,
                        to=to_call,
                        from_=from_call
                    )
print(call.sid)
