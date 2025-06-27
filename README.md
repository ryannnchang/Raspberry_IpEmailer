# Python Script Emailer

## Overview
This python script is intended to go on a Raspyberry Pi. When the Raspberry Pi boots up, it will send an email to alert the user of the Raspberry Pi's ip address. This is useful to connect to the Pi via VNC and the ip address keeps changing.

## Set up
### Step 1: Downloading the Script
1. Download the python script named “ip_checker.py”
2. Transfer the script onto your Raspberry Pi 
3. Place the file in your home directory on your Pi

Note: File will default download to your downloads folder

### Step 2: Setting up Gmail
In order to set up the python script, you will need to get access to your “App Password” to send emails from your gmail account. 

Note: This script will contain the login credentials for an email account. Anyone with root access to your machine will be able to retrieve these credentials. So I highly suggest you create a dummy account that is only used for sending these emails. 

1. Enable 2-step verification on your gmail account 
2. Go to: Create and manage your app passwords
3. Enter an App Name (Can be anything)

4. Copy the 16-digit password given to you (DO NOT SHARE)
5. On your raspberry pi, open up the script “ip_checker.py”
6. Under “Gmail Setup”, set SENDER_EMAIL, SENDER_PASS, RECEIVER_EMAIL equal to gmail of sender account, app password of sender account and gmail of receiver account respectively

7. Save the script by pressing “ctrl + s”
8. To test the script, enter “python ip_checker.py” in the terminal

Note: The script has a delay of 60 seconds to account to allow the Pi enough time to connect to wifi. You can adjust this to your setup by adjusting time.sleep(). I would not recommend going below 30 seconds. 

### Step 8: Running the automatically script when the Raspberry Pi boots up
1. Open up terminal on Raspberry Pi
2. Enter “chmod +x ip_checker.py”
3. Enter “crontab -e”
4. Choose 1 and hit enter (if asks)
5. Scroll to the bottom
6. Paste @reboot /usr/bin/python3 /home/username/ip_checker.py but replace username with your username
7. Hit “ctrl + x”
8. Hit “y”
9. Hit “enter”
   
Now you're done! Reboot your Pi and you should get an email with your ip address

