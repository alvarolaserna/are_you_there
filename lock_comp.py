from cv_recogn import *

def check_awake(input: int):
    # checks if there is someone using the camera
    while True:
        if not is_someone(input):
            import os
            os.system("pmset sleepnow")

if __name__ == "__main__":
    print("Welcome to the lock computer")
    # change the input depending on which one is your cam
    # in this case it uses 0, but sometimes it can be 1 or 2...
    check_awake(0)