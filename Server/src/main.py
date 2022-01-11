# lib import
from flask import Flask, redirect, url_for, jsonify, abort, request
from datetime import datetime
import json
# class import
from classes.sqlConnect import dataSet
from classes.logger import logger
from chicken import chicken as c
from chicken import chickens
from classes.device import device, deviceManager
from timeChecker import timeChecker as tC

# Create basic app
app = Flask(__name__)

# Logging
log = logger('test.txt', loglevel=0)

log.critical('test')
log.error('test2')

# Create deviceManger for list of connected devices
dM = deviceManager()

# @app.before_first_request
# def register():
#     if dM.device_by_ip(request.remote_addr):
#         return jsonify({
#                     "status": "succes",
#                     "code": "200",
#                     "message": "Device allready registered",
#                 }), 200
#     else:
#         return redirect(url_for('login'), 302)


status = {
    'food': 'fedded', # fedded -> fed?
    'door': 'closed'
}


"""             ROUTING             """


@app.route('/')
def rootIndex():
    # 301 - Permanent Redirect
    return redirect(url_for('apiIndex'), 301)


@app.route('/api')
def apiIndex():
    return jsonify({
        "status": "OK",
        "code": "200",
        "message": "Huehnerstall-API",
        "login": url_for('login'),
        "door_endpoint": url_for('door'),
        "food_endpoint": url_for('food')
    }), 200


@app.route('/api/door', methods=['POST'])
def door():
    if request.method == 'POST':
        status["door"] = request.form['status']
    else:
        abort(405)


@app.route('/api/food', methods=['POST'])
def food():
    if request.method == 'POST':
        status["food"] = request.form['status']
    else:
        abort(405)


@app.route('/api/login', methods=['POST'])
def login():
    if request.method == 'POST':
        #print(request.get_data(as_text=False))
        #x = json.loads(json.dumps(request.get_data(as_text=True)))
        #print(json.loads(request.get_data(as_text=True).replace("'","\""))['ip'])
        #print(json.loads(f'{request.get_data(as_text=True)}'))
        #tmp_device = device(ip=request.form['ip'], id=request.form['id'])
        tmp_device = device(ip=json.loads(request.get_data(as_text=True).replace("'","\""))['ip'], id=json.loads(request.get_data(as_text=True).replace("'","\""))['id'])
        if len(dM.devices) == 0:
            dM.add_device(tmp_device)
            return tmp_device.to_json(), 200
        else:
            if dM.is_inside(tmp_device):
                return jsonify({
                    "status": "success",
                    "code": "200",
                    "message": "Device already registered",
                }), 200
            else:
                dM.add_device(tmp_device)
                return tmp_device.to_json(), 200
        del tmp_device #wird druch return nicht ereicht, durch try-catch-finally block ersetzen
    else:
        abort(405)

#Anfrage Webserver, wo sich spez. Huhn befindet
@app.route('/chickenStatus/<int:id>')
def show_chicken_info(id: int):
    chicken: c = c(id)
    status = chicken.checkStatus()

    return status[0]

#Anfrage, ob alle Hühner im Stall sind
@app.route('/checkAll/')
def checkAllChicks():
    results = chickens().checkChicks()
    message = str(results[0]) + ' von ' + str(results[1]) + ' sind im Stall (Ort A).'

    if chickens().chickensInside() == True:
        message = message + ' Funktion bestätigt'


    return message

#Anfrage zur Aufnahme einer Sensoraktivität in DB
@app.route('/sensor/<int:id>/<string:arduino>')
def createDataSet(id: int, arduino: str):
    newDS: dataSet = dataSet(id, datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H-%M"), 1, arduino)
    newDS.uploadDataSet()

    return 'transmitted'


"""             Errorhandler             """


@app.errorhandler(404)
def ressource_not_found(error):
    return jsonify({
        "status": "error",
        "code": "404",
        "message": "Ressource not found",
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "status": "error",
        "code": "405",
        "message": "Methode not allowed",
    }), 405


# ensure interpreter assigns __name__ variable
if __name__ == '__main__':
    timeCheck = tC(False)
    timeCheck.checkTime()
    print('start?')
    app.run(host='0.0.0.0', port=5000)