# For the 4 inch raspberry pi screen and my leg.
# Count down from 30 seconds and flash the screen until the
# button is pushed and start over.
from guizero import App, Text, PushButton
from time import sleep, strftime, localtime

def countdown():
    global seconds_left
    global sleep_time

    while sleep_time < 1800:
        sleep(sleep_time)
        seconds_left = seconds_left - sleep_time
        time_of_day_text.text=strftime("%M:%S", localtime())

def reset_time():
    pass

# Create the window
counter_window = App(title="30 minute countdown timer", width=800, height=480)
time_of_day_text = Text(counter_window, text=strftime("%M:%S", localtime()))
time_left_text = Text(counter_window, text="30:00", size=60)
reset_button = PushButton(counter_window, text="Reset Counter", command=reset_time)
seconds_left = 1800
sleep_time = 5
reset_flag = False
countdown()


counter_window.display()
