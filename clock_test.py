import sys
from guizero import *
import time

def tick():
    global start_sec
    global button_bg
    time_string = time.strftime("%H:%M:%S %m/%d/%Y")
    # print(time_string)
    clock.value = time_string
    elapsed_seconds = int(time.time()) - start_sec
    minutes_left = 4 - elapsed_seconds // 60
    seconds_left = 60 - elapsed_seconds % 60
    if seconds_left == 60:
        minutes_left = minutes_left + 1
        seconds_left = 0
    seconds_display = str(seconds_left)
    # print(len(seconds_display))
    if len(seconds_display) == 1:
        seconds_display = "0" + seconds_display
    timer_display = "Time Left: " + str(minutes_left) + ":" + seconds_display
    timer.value = str(timer_display)
    if minutes_left < 2:
        if button_bg == "#D3D3D3":
            button_bg = "#FFCCCB"
        else:
            button_bg = "#D3D3D3"
        reset_button.bg = button_bg
    clock.after(200, tick)

def reset_time():
    global start_sec
    global button_bg
    button_bg = "#D3D3D3"
    print("reset pressed")
    start_sec = int(time.time())
    tick()

app = App(width=800, height=480)

clock = Text(app, size=55, bg="white", text="Time Left: " + time.strftime("%H:%M:%S"), width="fill", height=1)
timer = Text(app, size=55, bg="#90EE90", text="04:00", width="fill", height=2)
start_sec = int(time.time())
button_bg = "#D3D3D3"
reset_button = PushButton(app, command=reset_time, text="Reset", width="fill", height="fill")
reset_button.text_size = 50
reset_button.bg = button_bg
tick()


app.display()