from dotenv import load_dotenv
import os

#Tai cac bien tu file env
load_dotenv() 

sender_email = os.getenv("SENDER_EMAIL")
app_password = os.getenv("APP_PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")
