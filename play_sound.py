from threading import Thread
import time
from playsound import playsound

# Define a function for the thread
def thread1():
   playsound('lugangxiaozheng.m4a')

def play_sound():
    t = Thread(target=thread1)
    t.start()
    # time.sleep(5)
    print("sound played")

# play_sound()
