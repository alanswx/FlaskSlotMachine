from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect

app = Flask(__name__)


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
    print("Matches:"+str(matches))
    val = jsonify(
        spinAvailable=spinAvailable,
        status="Good"
    )
    return val

@app.route('/lose/')
def slotLose():
    global spinAvailable
    val = jsonify(
        spinAvailable=spinAvailable,
        status="Good"
    )
    return val
@app.route('/win/')
def slotWin():
    global spinAvailable
    val = jsonify(
        spinAvailable=spinAvailable,
        status="Good"
    )
    return val

@app.route('/')
def index():
    return redirect("/static/slot5/index.html")


