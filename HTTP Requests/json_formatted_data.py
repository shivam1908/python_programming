import requests

url = "https://icanhazdadjoke.com/"

response = requests.get("https://icanhazdadjoke.com/", headers = {"Accept" : "application/json"})

data = response.text # it will bring the json data in string format
print(f"Type of the json data fetched is : {type(data)}")
print(data)

# To fetch the json data as it is or dict format we need to use response.json()
# so we could directly fetch the info/ jokes form dict
data = response.json()
print(f"Type of data fetched using .json() is : {type(data)}")
print(data["joke"])