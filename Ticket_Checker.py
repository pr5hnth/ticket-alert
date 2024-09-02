import time
import requests
from bs4 import BeautifulSoup

# Telegram setup
bot_token = '7195218947:AAFEUOU-BQ69rNeuKZwmAbDN3PQfrqr9SBA'
chat_id = '891730654'
message = "GOAT Tickets for Thursday are now available!"

def send_telegram_alert():
    try:
        send_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
        response = requests.get(send_url)
        if response.status_code == 200:
            print("Telegram message sent successfully.")
        else:
            print(f"Failed to send message: {response.status_code}")
    except Exception as e:
        print(f"Error sending Telegram message: {e}")

def check_tickets(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example logic to find "Thursday"
        if 'Thu' in soup.text:
            send_telegram_alert()
        else:
            print("Thursday tickets not available yet.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    urls = [
        "https://paytm.com/movies/chennai/varadaraja-cinemas-4k-rgb-laser-dolby-atmos-c/3952",
        "https://in.bookmyshow.com/buytickets/kckrishnavenicinemas-rg3-laser-dolbyatmos-tnagar/cinema-chen-KVCS-MT/20240903"
    ]

    while True:
        for url in urls:
            check_tickets(url)
        time.sleep(7)  # Wait for 7 seconds before checking again
