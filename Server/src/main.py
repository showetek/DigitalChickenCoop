#lib import
from flask import Flask, redirect, url_for, jsonify, abort, request
from markupsafe import escape
from datetime import datetime
from pprint import pprint

from werkzeug.datastructures import Range
#class import
from classes.sqlConnect import dataSet
from classes.chicken import chicken
from classes.device import device, deviceManager

#Create basic app
app = Flask(__name__)

#Create deviceManger for list of connected devices
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
    
"""             ROUTING             """

@app.route('/')
def rootIndex():
    # 301 - Permanent Redirect
    return redirect(url_for('apiIndex'), 301)

@app.route('/api')
def apiIndex():
    return 'OK', 200

@app.route('/api/login', methods=['POST'])
def login():
    if request.method == 'POST':
        tmp_device = device(ip=request.form['ip'], id = request.form['id'])
        if len(dM.devices) == 0:
            dM.add_device(tmp_device)
            return tmp_device.to_json(), 200
        else:
            if dM.is_inside(tmp_device):
                return jsonify({
                    "status": "succes",
                    "code": "200",
                    "message": "Device allready registered",
                }), 200
            else:
                dM.add_device(tmp_device)
                return tmp_device.to_json(), 200
    else:
        abort(405)

@app.route('/chicken/<int:c_number>')
def show_chicken_info(c_number):
    return 'You choose chicken number: {0}'.format(escape(c_number))

@app.route('/action/<int:id>/<string:arduino>')
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
    app.run(host='0.0.0.0', port=5000)

