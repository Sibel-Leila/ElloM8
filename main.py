from twilio.rest import Client
from jokeapi import Jokes
import csv

# constants
account_sid = ''
auth_token = ''
to_call = '+'
from_call = '+'
path = ''

def read_numbers():
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(f'We are calling the number: {row[0]}')
            send_jokes(row[0])

def send_jokes(number):
    # Create the joke
    j = Jokes()
    joke = j.get_joke(lang='en',
                    category=['misc', 'pun', 'spooky', 'christmas'],
                    blacklist=['nsfw', 'religious', 'political', 'racist', 'sexist'])
                    # Retrieve a random joke

    # Create the response
    if joke['type'] == 'single':
        print(joke['joke'])
        response = '<Response><Say>' + joke['joke'] + '</Say></Response>'
    else:
        print(joke['setup'])
        print(joke['delivery'])
        response = '<Response><Say>' + joke['setup'] +  '</Say><Pause length="3"/><Say>' + joke['delivery'] + '</Say></Response>'

    # Call the person

    client = Client(account_sid, auth_token)
    call = client.calls.create(
                            twiml=response,
                            to=number,
                            from_=from_call
                        )
    print(call.sid)

if __name__ =='__main__':
    read_numbers()
