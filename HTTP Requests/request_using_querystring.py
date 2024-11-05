import requests


url = "https://icanhazdadjoke.com/search"
print("Hello There Lets joke around!")
user_search= input("Please enter the new term to search joke on: ")
while True:
    response = requests.get(
        url,
        headers = {"Accept" : "application/json"},
        params ={"term" : user_search , "limit" : 1}
    )
    data = response.json()
    if data['total_jokes']:
        joke = data["results"][0]['joke']
        print(joke)
        break
    user_search = input("No Joke Found.Please enter the new term to search joke on: ")

