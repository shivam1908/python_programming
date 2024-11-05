import requests

url = "https://icanhazdadjoke.com/"
#Acceptable format to plain text instead of html for this website
response = requests.get(url,headers ={"Accept" : "text/plain"})
print(response.text)