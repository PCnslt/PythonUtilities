from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time, os
from dotenv import load_dotenv



load_dotenv('.secrets')
monster_username = os.getenv('MONSTER_USER')

service = Service('chromedriver')

service = Service()
def get_drvier():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://www.monster.com/")
  return driver

def clean_text(text):
    """Extract only the temperature value."""
    return float(text.split(': ')[1])

def main():
  driver = get_drvier()
  time.sleep(2)
#   element = driver.find_element(by="xpath", value="//h1")
  element = driver.find_element(by="xpath", value="//*[@id='displaytimer']/div")
  return clean_text(element.text)

print(main())