import requests

url = "http://127.0.0.1:5001/invocations"

data = {
    "dataframe_records": [
        {
            "age": 22,
            "fare": 7.25,
            "sex": 1,
            "sibsp": 1,
            "parch": 0,
            "pclass": 3,
            "embarked": 0
        }
    ]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)

print("Prediction Result:")
print(response.json())