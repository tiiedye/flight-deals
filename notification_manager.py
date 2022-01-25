from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_VIRTUAL_NUM = os.getenv("TWILIO_NUM")
TWILIO_VERIFIED_NUM = os.getenv("MY_NUM")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUM,
            to=TWILIO_VERIFIED_NUM,
        )
        print(message.sid)
