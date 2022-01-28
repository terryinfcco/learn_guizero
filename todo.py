# Write your code here :-)
# Guizero book, Chapter 1
# import guizero library

from guizero import App, Text, ListBox, PushButton
# Create the app main window - can be called whatever
# Put a title on the window.

def edit_button():
    if title_list.value != "":
        print(title_list.value)
def new_item():
    pass

app = App(title="To Do List", height=800, width=480, layout="grid")
# Add a text widget

message = Text(app, text="Terry To Do List", size=18, grid=[0,0])

title_list = ListBox(app, height=600, width=475, items=["1 - Write Todo List", "2 - Test Todo List"], grid=[0,1,2,1])
title_list.text_size = 14

edit_button = PushButton(app, text="Edit Selected", command=edit_button, grid=[0,2], width="fill")
edit_button.text_size = 16

new_button = PushButton(app, text="New Todo Item", command=new_item, grid=[1,2], width="fill")
new_button.text_size = 16
app.display()