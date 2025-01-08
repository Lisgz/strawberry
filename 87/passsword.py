
import random

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789!@#$%^&*()"

while 1:
    password_len = int(input("what length of password: "))
    password_count = int(input("how many options: "))
    for x in range(0, password_count):
        password = ""
        for y in range(0,password_len):
            password_char = random.choice(chars)
            password     = password + password_char
        print("Password: ", password)