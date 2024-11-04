#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


pip install aiohttp


# In[6]:


import asyncio
import aiohttp
import json


API_KEY = "38f34d9bbc83a5a3ad50db45380a0183"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


async def fetch_weather(city, unit="C"):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"  
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return format_weather(data, unit=unit) 
            elif response.status == 404:
                return f"City '{city}' not found."
            else:
                return f"Could not fetch weather for {city} (Status: {response.status})"


def format_weather(data, unit="C"):
   
    temp_celsius = data["main"]["temp"]

    
    if unit == "F":
        temp = temp_celsius * 9 / 5 + 32
    elif unit == "K":
        temp = temp_celsius + 273.15
    else:
        temp = temp_celsius 

   
    city = data["name"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

   
    return (f"Weather in {city}:\n"
            f"- Temperature: {temp:.2f}°{unit}\n"
            f"- Condition: {description.capitalize()}\n"
            f"- Humidity: {humidity}%\n")


async def main(cities, unit="C"):
    tasks = [fetch_weather(city, unit=unit) for city in cities]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


cities = ["New York", "London", "Tokyo", "Sydney"]
unit = "F"  


await main(cities, unit=unit)


# In[ ]:




