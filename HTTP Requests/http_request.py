
import requests

response = requests.get("https://www.msn.com/en-in/news")
print(response.status_code)
print(response.headers)