import os 
from langchain_community.utilities import openweatherAPIWrapper
os.environ["OPENWEATHER_API_KEY"] = "4aba8816ce33cf53bdc8e8c67343a3f0"
weather=OpenweatherAPIWrapper()
loaction= input("enter the location:")
result=weather.run('shimla')
print(result)
