import requests
from datetime import datetime


sheety_get_endpoint = "https://api.sheety.co/ec81f9b66c2640a5ac734bf15dee2f0d/myWorkouts/workouts"
sheety_post_endpoint = "https://api.sheety.co/ec81f9b66c2640a5ac734bf15dee2f0d/myWorkouts/workouts"
BEARER_TOKEN = "Bearer 32e3rweegnfhgmty543rfegtfhn"

APP_ID = "ed4d9445"
API_KEY = "f35d7ef8bca9732492a119c76e34a40f"


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {"x-app-id": APP_ID, "x-app-key": API_KEY, "Content-Type": "application/json"}

prams = {
"query": input("Tell me which exercise you did: "),
 "gender": "male",
 "weight_kg": 68.5,
 "height_cm": 178.64,
 "age": 20
}

date = datetime.now().strftime("%d/%m/%Y")
print(date)
time = datetime.now().strftime("%X")
print(time)

response = requests.post(url=nutritionix_endpoint, json=prams, headers=header)
print(response.status_code)
result = response.json()
print(result)

sheety_json = {"workout": {
 "date": date,
 "time": time,
 "exercise": response.json()['exercises'][0]['name'],

 "calories": response.json()['exercises'][0]['nf_calories']
 }
 }

sheety_header = {"Content-Type": "application/json", "Authorization": BEARER_TOKEN}

sheety_response = requests.post(url=sheety_post_endpoint, json=sheety_json, headers=sheety_header)
print(sheety_response.status_code)
