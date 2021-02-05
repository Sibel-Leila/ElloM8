from jokeapi import Jokes
j = Jokes()  # Initialise the class
joke = j.get_joke(lang='en',
                category=['misc', 'pun', 'spooky', 'christmas'],
                blacklist=['nsfw', 'religious', 'political', 'racist', 'sexist']) # Retrieve a random joke
# pprint.pprint(joke)
if joke['type'] == 'single': # Print the joke
    print(joke['joke'])
else:
    print(joke['setup'])
    print(joke['delivery'])
