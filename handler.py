import os
from urllib.parse import urlencode

from twilio.rest import Client


def handler(event=None, context=None):
    client = Client(
        os.environ['TWILIO_ACCOUNT'],
        os.environ['TWILIO_TOKEN'],
    )

    for phone in os.environ.get('ALERT_PHONES', '').split(','):

        call = client.calls.create(
            to=phone,
            from_=os.environ['TWILIO_PHONE'],
            url='http://twimlets.com/message?{}'.format(urlencode({
                'Message[0]': "Baby needs to go potty",
            })),
        )

        print(call.sid)


if __name__ == "__main__":
    handler()
