#Property of Thinker Designs
#Property of AZ Buy Corp
import json
#variables
print("This is a python file where it will take an input and make it into a json format which was made by The Thinker part of Thinker Designs and Automation and AZ Buy Corp")
name = input('Enter the name:')
age = input('Enter the age:')
address = input('Enter the address:')
email = input('Enter the email:')
y = {
    "name": name,
    "age": age,
    "address": address,
    "email": email
}
b = json.dumps(y)
print(b)