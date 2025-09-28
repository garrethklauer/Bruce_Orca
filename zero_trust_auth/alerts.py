from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_slack_alert(token: str, channel: str, message: str):
    client = WebClient(token=token)
    try:
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Slack error: {e.response['error']}")