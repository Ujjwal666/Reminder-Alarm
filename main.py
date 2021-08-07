import random
import time
import json
from tkinter import *
import time
import datetime
import winsound
from threading import *
from gtts import gTTS
import webbrowser
import os

root = Tk()
root.geometry("300x400")
root.configure(background='black')
root.title("Reminder Alarm")


# Use Threading
def Threading():
    t1 = Thread(target=check_status)
    t1.start()

def instructor():
    instruct_window = Toplevel(root)
    instruct_window.title("Instruction")
    instruct_window.geometry("250x250")
    instruct_window.configure(background='black')
    first = Text(instruct_window, fg="steel blue", bg='black',font=( 'aria' ,10, 'bold' ))
    first.insert(INSERT, "1. Write the hours and minutes in the respective fields and the time period in (am/pm) format at what time you want the alarm to be set."+"\n"+"\n"+""
                        "2. Write whats your purposse of the alarm in the message field so we could let you remember about it through speech else we would play a music video.")
    first.pack(expand=True, fill=BOTH)

def check_status():
    print("entered")
    while True:
        hours = hours_input.get("1.0", "end-1c")
        minutes = minutes_input.get("1.0", "end-1c")
        time_period = time_period_input.get("1.0", "end-1c")
        message = message_input.get("1.0", "end-1c")

        if time_period == "pm":
            hours = int(hours) + 12

        if len(str(hours)) == 1:
            hours = "0" + str(hours)
        if len(minutes) == 1:
            minutes = "0" + str(minutes)

        user_time = str(hours) + ":" + str(minutes)

        time.sleep(1)

        print(hours, minutes, time_period, message)

        current_time = datetime.datetime.now().strftime("%H:%M")

        print(current_time, user_time)

        if current_time == user_time:
            if len(message) != 0:
                print("Time for", message)
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

                speak_message = gTTS(text=message, lang='en', slow=False)
                speak_message.save("speak_message.mp3")
                os.system("start speak_message.mp3")
                time.sleep(20)
                continue
            else:
                file = open('youtubleLink.json')
                url = json.load(file)
                rand_url = random.choice(url["url"])
                print(rand_url)
                webbrowser.open(rand_url)
                break


        # print(current_time)
        # print("user",user_time)

title = Label(root, font=( 'aria' ,20, 'bold' ),text="Reminder Alarm",anchor='n',fg="steel blue",bg='black')

text_hour = Label(root, font=( 'aria' ,10, 'bold' ),text="Input the hour",anchor='n',fg="steel blue",bg='black')
hours_input = Text(root, height=1, width=3, bg="white", padx=50, pady=5)

text_minute = Label(root, font=( 'aria' ,10, 'bold' ),text="Input the minute",anchor='n',fg="steel blue",bg='black')
minutes_input = Text(root, height=1, width=3, bg="white",padx=50, pady=5)

text_period = Label(root, font=( 'aria' ,10, 'bold' ),text="Input the time period",anchor='n',fg="steel blue",bg='black')
time_period_input = Text(root, height=1, width=3, bg="white",padx=50, pady=5)

text_message = Label(root, font=( 'aria' ,10, 'bold' ),text="Input the message for alarm",anchor='n',fg="steel blue",bg='black')
message_input = Text(root, height=5, width=10, bg="white",padx=60)

set_button = Button(root, font=( 'aria' ,10 ), text="Set Alarm", fg="steel blue",bg='black', command=Threading)

instructions = Button(root, font=( 'aria' ,10 ),text="Instructions",anchor='n',fg="steel blue",bg='black',command= instructor)

title.pack()

text_hour.pack(side=TOP,anchor="n")
hours_input.pack(anchor="n")

text_minute.pack(side=TOP, anchor="n")
minutes_input.pack(anchor="n")

text_period.pack(side=TOP, anchor="n")
time_period_input.pack(anchor="n")

text_message.pack(side=TOP, anchor="n")
message_input.pack(anchor="n")

set_button.pack(anchor="n",pady=10,padx=10)

instructions.pack(side=BOTTOM,anchor="e")

root.mainloop()
