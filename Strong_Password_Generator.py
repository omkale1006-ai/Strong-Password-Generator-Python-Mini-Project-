# making a strong password minim project for security.

# import the random modul
import random


strong_pass="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!$%&'()*+,-./:;<=>?@[\]^_`{|}~1234567890"
strong_password=""

try:
    user_password_number=int(input("Enter your password length:- "))

    for i in range(user_password_number):
            strong_password += random.choice(strong_pass)
    print(strong_password)
except ValueError:
      print("give the lenght of password!, in a numbers")