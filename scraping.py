import urllib2
from bs4 import BeautifulSoup
import requests
from twilio.rest import TwilioRestClient

url = 'https://github.com/Cheese810/test/issues/2'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip()
account_sid = 'XXX'
auth_token = 'XXX'
twilio_phone_number = '+15037571538'
my_phone_number = '+15037571538'

webpage = requests.get(url)
soup = BeautifulSoup(webpage.text, 'html.parser')
print(soup)

> = [s for s in soup.body.stripped_strings if 'free' in s.lower()]

if >
body = 'It worked!'

client = TwilioRestClient(account_sid, auth_token)

client.messages.create(
    body="Hello World!",
    to=my_phone_number,
    from_=twilio_phone_number
)