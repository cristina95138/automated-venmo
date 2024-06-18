from twilio.rest import Client
import os

def send_sms(api_key, api_secret, twilio_phone_number, phone_number, message):
    client = Client(api_key, api_secret)

    try:
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=phone_number
        )
        print(f"SMS sent successfully.")
    except Exception as e:
        print(f"Failed to send SMS. Error: {str(e)}")

def main():
    api_key = os.getenv("TWILIO_ACCOUNT_SID")
    api_secret = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
    phone_numbers = os.getenv("PHONE_NUMBERS").split(",")  # Split phone numbers by comma
    message = "https://venmo.com/?txn=pay&audience=public&recipients=CristinaLawson&amount=5&note=sppotify"
    
    for number in phone_numbers:
        number = number.strip()  # Remove any leading/trailing whitespace
        send_sms(api_key, api_secret, twilio_phone_number, number, message)

if __name__ == "__main__":
    main()
