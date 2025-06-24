#!/usr/bin/env python3
import smtplib
import socket
import time
from email.mime.text import MIMEText
import subprocess

time.sleep(60)


# Gmail setup
SENDER_EMAIL = "Enter Sender Email Address"
SENDER_PASS = "Enter Sender Email App Password"
RECEIVER_EMAIL = "Enter Receiver Email Address"

# Get hostname and IP
def get_ip():
    try:
        result = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE)
        ip = result.stdout.decode().strip().split()[0]
        return ip
    except Exception as e:
        print(f'Error getting ip: {e}')
        ip = "Unavailable"
    

hostname = socket.gethostname()
ip_address = get_ip()

# Compose email
subject = f"{hostname}'s IP Address"
body = f"Current Pi's IP address: {ip_address}"

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = SENDER_EMAIL
msg['To'] = RECEIVER_EMAIL

# Send email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASS)
        server.send_message(msg)
    print("IP sent successfully!")
except Exception as e:
    print(f"Failed to send IP: {e}")
