import pyautogui
import random
import string

def brute_force():

    char=list(string.ascii_letters)
    print(char)
    password=pyautogui.password("Enter password here:")

    guess_password=''
    while (guess_password!=password):
        guess_password=random.choices(char,k=len(password))

        print(">>>>>"+str(guess_password)+"<<<<<")

        if(guess_password==list(password)):
            print("Your password is : " + "".join(guess_password))
            break
