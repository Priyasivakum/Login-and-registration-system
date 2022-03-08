import os
import pandas
def welcome():
    print("HI user,Welcome!")
    W=input("Login|Register[L/R]: ")
    if W=="L":
        login()
    elif W=="R":
        register()
    else:
        print("Choose the valid option please...")
        welcome()
welcome()