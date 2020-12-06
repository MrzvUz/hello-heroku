from flask import FLask
app = FLask(__name__)

@app.route('/')
def index():
    return "Hello, Smart Pension!"