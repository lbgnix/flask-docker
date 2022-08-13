from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}
COLOR_FROM_ENV = os.environ.get('APP_COLOR')
VERSION_FROM_ENV = os.environ.get('VERSION') or "v1"
IP_FROM_ENV = os.environ.get('IP')
COLOR = random.choice(["red", "green", "blue", "blue2", "darkblue", "pink"])

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', name=socket.gethostname(), ip=host_ip, color=color_codes[COLOR], version=VERSION_FROM_ENV)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
