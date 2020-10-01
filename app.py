import requests
from config import sid, auth_token, sensor
from twilio.rest import Client

client = Client(sid, auth_token)

def send_message(is_safe, aqi_value):

	if is_safe:
		client.messages.create(to="+14152997994", from_='+12056795299', body=f'Air quality has reached an acceptable level of {aqi_value}.')
	else:
		client.messages.create(to="+14152997994", from_="+12056795299", body=f'Warning: air quality is at {aqi_value}.')

def check_quality():
	url = 'https://www.purpleair.com/json?show=' + sensor
	air_data = requests.get(url).json()
	pm_value = float(air_data['results'][0]['PM2_5Value'])
	print(pm_to_aqi(pm_value))

def pm_to_aqi(pm_value):

	def calc_aqi(Cp, Ih, Il, BPh, BPl):
		a = (Ih - Il)
		b = (BPh - BPl)
		c = (Cp - BPl)
		return round((a/b)*c+Il)
		
	if pm_value < 0:
		return 0
	elif pm_value > 1000:
		return None
	elif pm_value > 350.5:
		return calc_aqi(pm_value, 500, 401, 500, 350.5)
	elif pm_value > 250.5:
		return calc_aqi(pm_value, 400, 301, 350.4, 250.5)
	elif pm_value > 150.5:
		return calc_aqi(pm_value, 300, 201, 250.4, 150.5)
	elif pm_value > 55.5:
		return calc_aqi(pm_value, 200, 151, 150.4, 55.5)
	elif pm_value > 35.5:
		return calc_aqi(pm_value, 150, 101, 55.4, 35.5)
	elif pm_value > 12.1:
		return calc_aqi(pm_value, 100, 51, 35.4, 12.1)
	else: 
		return calc_aqi(pm_value, 50, 0, 12, 0)
check_quality()
