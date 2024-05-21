import requests
import os
from datetime import datetime

# https://docs.google.com/spreadsheets/d/1gMYzwnsA7rv3R0_YQ7Fw4Lu6KwgfQcAbCqBKJJz5GhA/edit#gid=0

APP_ID = os.getenv('NUTRITION_USER')
API_KEY = os.getenv('NUTRITION_API')
SHEETY_AU = os.getenv('SHEETY_Bearer_Authentication')
POST_SHEETY = os.getenv('POST_SHEETY_END_POINT')

GENDER = 'male'
WEIGHT_KG = '81'
HEIGHT_CM = '176'
AGE = '24'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
print(sheet_inputs)


bearer_headers = {
"Authorization": f"Bearer {SHEETY_AU}"
}
sheet_response = requests.post(POST_SHEETY, json=sheet_inputs, headers=bearer_headers)
print(sheet_response.text)