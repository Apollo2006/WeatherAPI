import requests
from dhooks import Webhook

hook = Webhook('https://discord.com/api/webhooks/1001605987922354286/AUwsrc_Q8XMDlXbiukBxF3j02dzs_AS9wZ4Dkvr__zA2EbgmOW3FQYE1jsNtDPhCXiYl')
API_KEY = '4b7ea539bbcff48519b85f5d12d315a3'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = 'new york'
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}&units=imperial'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print("Weather: ", weather)
    hook.send(weather)
    temperatue = data['main']['temp']
    print("Temperatue: ", temperatue, "F")
else:
    print('An error occured')