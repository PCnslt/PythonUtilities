from dotenv import load_dotenv
import os, requests

load_dotenv('.secrets')

facebook_utility_app_key = os.environ('FACEBOOK_UTILITY_APP_KEY')
url = f"https://graph.facebook.com/v22.0/me?fields=id%2Cname&access_token={facebook_utility_app_key}"

response = requests.get(url, timeout=120)
print(response.text)
