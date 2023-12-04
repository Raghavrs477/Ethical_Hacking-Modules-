import os

VONAGE_API_KEY = os.environ['VONAGE_API_KEY']
VONAGE_API_SECRET = os.environ['VONAGE_API_SECRET']

#Create a client instance and then pass the client to the Sms instance
client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
sms = vonage.Sms(client)
response = sms.send_message(
    {
        "from": VONAGE_BRAND_NAME,
        "to": TO_NUMBER,
        "text": "Hello there from Vonage SMS API",
    }
)

if response["messages"][0]["status"] == "0":
    print("Message Details: ", response)
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {response['messages'][0]['error-text']}")
