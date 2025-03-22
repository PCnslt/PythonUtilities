from dotenv import load_dotenv
import os, requests, json

load_dotenv('.secrets')

facebook_utility_app_key = os.getenv('FACEBOOK_UTILITY_APP_KEY')
url = f"https://graph.facebook.com/v22.0/10153886934964706/picture?access_token={facebook_utility_app_key}"
response = requests.get(url, timeout=120)

data = json.loads(response.text)
print(data)
