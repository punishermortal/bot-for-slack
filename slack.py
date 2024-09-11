from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import schedule
import time

# Replace with your Slack bot token
client = WebClient(token="")

# user_id = "U073G73BQRE"
user_id = "UMGT1E8A0"

def send_daily_message():
    try:
        response = client.chat_postMessage(
            channel=user_id,  
            text="Hello! This is your daily reminder!"
        )
        print(response)
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

# Schedule the job to run daily at a certain time (e.g., 9 AM)
# schedule.every().day.at("09:00").do(send_daily_message)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


send_daily_message()
