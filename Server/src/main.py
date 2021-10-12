#lib import
from flask import Flask, redirect, url_for, jsonify, abort, request
from markupsafe import escape
#class import
from classes.sqlConnect import dataSet
from classes.chicken import chicken
from classes.device import device

#Create basic app
app = Flask(__name__)

"""             ROUTING             """

@app.route('/')
def rootIndex():
    # 301 - Permanent Redirect
    return redirect(url_for('apiIndex'), 301)

@app.route('/api')
def apiIndex():
    return 'OK', 200



@app.route('/chicken/<int:c_number>')
def show_chicken_info(c_number):
    return 'You choose chicken number: {0}'.format(escape(c_number))

@app.route('/action/<int:id>')
def createDataSet(id: int):
    newDS: dataSet = dataSet(id, '12.10.21', '10:30', True)
    newDS.uploadDataSet()

    return 'transmitted' + str(id)

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

