import requests

def getUsers():
  try:
    response = requests.get("http://localhost:3000/")
    for element in response.json():
      print()
      for key in element:
        print(f"{key.capitalize()}: {element[key]}")
  except: print("Error in Get Users")

def addUser():
  try:
    name = input("Enter user's name: ")
    password = input("Enter user's password: ")
    data = { "name": name, "password": password }
    response = requests.post("http://localhost:3000/add", json=data)
    print(response.json())
  except: print("Error in Add User")

def main():
  option = 'Y'
  while True:
    print("\n1. Get Users\n2. Add User")
    choice = input("Enter choice: ")
    if choice == '1': getUsers()
    elif choice == '2': addUser()
    else: print("Invalid choice.")
    option = input("\nDo you want to continue? ")[0]
    if option in 'nN':
      print("Exiting.")
      break

main()