import requests

def getRequest():
  try:
    response = requests.get("http://localhost:3000/")
    print(response.json())
  except: print("Error")

def postRequest():
  try:
    data = { "name": "ABC", "age": 10 }
    response = requests.post("http://localhost:3000/", json=data)
    print(response.json())
  except: print("Error")