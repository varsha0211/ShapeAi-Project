import requests
#import os
from datetime import datetime

api_key = ''
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

with open('output.txt','w') as f:
    f.write("-------------------------------------------------------------\n")
    f.write("Weather Stats for - "  + format(location.upper()) +  " | " + format(date_time) + "\n" ) 
    f.write("-------------------------------------------------------------\n")
    f.write("\nCurrent temperature is: " + format(temp_city) + " deg C\n")
    f.write("Current weather desc  : " + format(weather_desc) +  "\n" )
    f.write("Current Humidity      : " + format(hmdt) + " %\n")
    f.write("Current wind speed    : " + format(wind_spd) + " kmph\n")
