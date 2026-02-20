from V7ACC import main_menu
import threading

# Start web server for monitoring
from flask import Flask, render_template_string
app = Flask('')

@app.route('/')
def home():
    return "KNX Generator Running - Check Console"

threading.Thread(target=app.run, kwargs={'host':'0.0.0.0','port':8080}).start()

# Start generator
main_menu()
