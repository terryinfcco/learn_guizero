# Write your code here :-)
# Guizero book, Chapter 1
# import guizero library
from guizero import App, Text
# Create the app main window - can be called whatever
# Put a title on the window.
app = App(title="Hello world")
# Add a text widget
message = Text(app, text="Welcome to the app")
app.display()