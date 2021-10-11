from flask import Flask, redirect, url_for
from markupsafe import escape
from classes.com import Com
#import Com
from classes.chicken import chicken

app = Flask(__name__)

@app.route('/')
def rootIndex():
    # 301 - Permanent Redirect
    return redirect(url_for('apiIndex'), 301)

@app.route('/api')
def apiIndex():
    #newCom = com(1)
    return 'OK', 200

@app.route('/chicken/<int:c_number>')
def show_chicken_info(c_number):
    print('TEST')
    return 'You choose chicken number: {0}'.format(escape(c_number))

@app.route('/communication')
def submitData():
    #testcode - hat eigentlich kein sinn
    newCom = Com()
    newCom.name = "11.10.2021-11:49"
    newCom.test = 3
    newCom.chickenID = [1]
    newCom.uploadCom()
    return 'transmitted'


@app.errorhandler(404)
def page_not_found(error):
    return '404: Page not found', 404

# ensure interpreter assigns __name__ variable
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

