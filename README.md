# ElloM8
Presentation: https://www.youtube.com/watch?v=pGR8OqSHAXo&feature=youtu.be

# Inspiration
Our family and friends isolating during COVID19 have been our inspiration for this project. Humor is an essential coping tool for surviving tough times. We could all use a few moments in the day that feel lighter, and a well-timed pandemic joke might just take your mind off the apocalypse-adjacent state of the world and serve as a reminder that there’s always something, however small, to smile about.

# What it does
The application calls people and tells them random jokes at a particular time each day.

# How we built it
We used Twilio's API to program the application to call people and set up text to speech.

We are currently using a Google Form to collect phone numbers. The spreadsheet is then downloaded as a csv file on our local machine(s) and the path is provided to the application. The Jokes API generates random jokes and using Twilio's text-to-speech capabilities, the application calls a user from the csv provided and reads the random joke. Using Google Cloud as a server for the application, we scheduled a cron job that would run this script at a particular time every day.

# Challenges we ran into
Understanding Twilio Interactive Voice Response and providing Google sheets responses to the application.

# Accomplishments that we're proud of
We managed to call some of our family members who are isolating in a hospital or at home and made them laugh.

# What we learned
Technology can really bring a smile to someone's face.

# What's next for 'Ello M8
The next step would be to provide the responses from the Google form to the application and call the user at a particular time provided by them in the form response. 'Ello M8 could also be further developed to send SMS to people with funny or inspiring quotes for the day and help set voice and SMS reminders for people who need to take medication on time and tell them a joke.

# Background:
We took part in https://impracticalhackers.devpost.com/?ref_content=default&amp;ref_feature=challenge&amp;ref_medium=discover and we created the project: 'Ello M8 - https://devpost.com/software/ello-m8

