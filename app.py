from flask import Flask, render_template, jsonify
import numpy as np
import requests
import RPi.GPIO as GPIO
import json

app = Flask(__name__)

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

# GPIO.setup(2, GPIO.IN)
# GPIO.input(17, GPIO.LOW)


@app.route("/testcall", methods = ["POST"])


# def update_call():
#     rand_num = np.random.rand(1)
#     return jsonify("", render_template("rand_num.html", x = rand_num))

    
@app.route("/dogApi", methods=["GET", "POST"])
def dog():
    url = f"https://dog.ceo/api/breeds/image/random"
    req = requests.get(url)
    obj = req.json()
    dog_pic = obj
    message = dog_pic["message"]
    print(dog_pic)
    print(message)

    return jsonify(message)

@app.route("/")
def start():

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80, debug = True)


