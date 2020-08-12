from fbchat import  Client, log
from fbchat.models import *
import apiai, codecs, json
import random

class Jarvis(Client):

    # Connect to dialogflow
    def apiaiCon(self):
        self.CLIENT_ACCESS_TOKEN = "EAAGnBnha5ksBAIGXBXJGR9Mwi4oDF5XvKrfcrE4gWuiobtESfC0NqhBaZBfBDbK349HrboykX5zZBMdIoYayPSf7pYsXV7YIuu3XeZBO0RI4WCdTI0wzIxhPwqsOWOOPGvZAChDvqTYB3fpZBAAMQYPgWpPXmSZAs8WIaZAn4V1yAZDZD"

        self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
        self.request = self.ai.text_request()
        self.request.lang = 'de' #Default : English
        self.request.session_id = "100036927017130"

    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        self.markAsRead(author_id)



        # Print info on console
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))

        # Establish conn
        self.apiaiCon()

        # Message Text
        msgText = message_object.text



        sample_responses = ["شوف انا جاي ياك نعاونك ف الزرك", "شوف اعرف انك مسؤول عن صوتك و عسك من تزرك لحد ما فيه المصلحة لموريتاني.", "صوت #لفلان اخير فيك ليهي اوفر للمواطنين لطباب يتعالج فيهم...إلخ ", "و السلام:)"]
        msg=random.choice(sample_responses)
        print('----->',msg)
        self.send(Message(text=msg), thread_id=author_id, thread_type=thread_type)


        # Request query/reply for the msg received
        self.request.query = msgText

        # Get the response which is a json object
        response = self.request.getresponse()
        output = self.request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
               if message.get('message')=='hi':
                   n=10
                   i=0
                   while(i<n):
                       print('*******how?********')
                       i=i+1



        # Convert json obect to a list
        reader = codecs.getdecoder("utf-8")
        obj = json.load(reader(response))


        # Get reply from the list
        reply = obj['result']['fulfillment']['speech']
        print('*******',reply)

        # Send message
        if author_id!=self.uid:
            print('----->',author_id)
            self.send(Message("hi"), thread_id=author_id, thread_type=thread_type)

        # Mark message as delivered
        self.markAsDelivered(author_id, thread_id)

    def get_message():
        sample_responses = ['how','did you']
        # return selected item to the user
        return random.choice(sample_responses)

# Create an object of our class, enter your email and password for facebook.
client = Jarvis('+212617958639', 'innov.it!@')


# Listen for new message
client.listen()