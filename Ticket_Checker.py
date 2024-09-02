import time
import requests
from bs4 import BeautifulSoup
import os
import smtplib
from email.mime.text import MIMEText

from keep_alive import keep_alive
keep_alive()

# Email setup
smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_user = 'mashrajnetflix@gmail.com'
email_password = 'geqsqyjooaesgqvo'
recipient_email = 'xenonrecords1@gmail.com'

def send_email_alert():
    try:
        msg = MIMEText("Tickets for Thursday are now available!")
        msg['Subject'] = 'IMP: Urgent!: GOAT Ticket Alert'
        msg['From'] = email_user
        msg['To'] = recipient_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(email_user, recipient_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def check_tickets():
    try:
        url = "https://paytm.com/movies/chennai/varadaraja-cinemas-4k-rgb-laser-dolby-atmos-c/3952"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example logic to find "Thursday"
        if 'Thu' in soup.text:
            send_email_alert()
        else:
            print("Thursday tickets not available yet.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        check_tickets()
        time.sleep(5)  # Wait for 5 seconds before checking again
