from __future__ import division
import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO

from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect


import time

# Import the PCA9685 module.
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
# Configure min and max servo pulse lengths
servo_min = 370  # Min pulse length out of 4096
servo_max = 575  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

def dispenseCoin(number):
    print("dispense coin"+str(number))
    for i in range(number):
      print("dispense one coin")
      pwm.set_pwm(0, 0, servo_max)
      time.sleep(1)
      pwm.set_pwm(0, 0, servo_min)
      time.sleep(1)


app = Flask(__name__)
socketio = SocketIO(app)


#
#  actions needed
#

spinAvailable=True


#
#  status -- when someone pulls the handle, we need to know
#

@app.route('/status/')
def status():
    global spinAvailable
    val = jsonify(
        spinAvailable=spinAvailable,
        status="Good"
    )
    spinAvailable = False
    return val

@app.route('/handlepulled/')
def handlePulled():
    global spinAvailable
    spinAvailable = True
    val = jsonify(
        spinAvailable=spinAvailable,
        status="Good"
    )
    return val

@app.route('/results/')
def slotResults():
    global spinAvailable
    matches=request.args.get('matches')
    num=int(matches)
    print("Matches:"+str(num))
    print(" before dispense")
    dispenseCoin(num+1)
    print("after dispense")
    val = jsonify(
        spinAvailable=spinAvailable,
        status="Good"
    )
    return val


@app.route('/')
def index():
    return redirect("/static/slot5/index.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)

