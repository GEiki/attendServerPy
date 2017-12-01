from flask import Flask
from flask import jsonify
from flask import request

import SQLUtil
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass


@app.route('/getuserinfo', methods=['GET', 'POST'])
def getuserinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        try:
            result = SQLUtil.getUserinfo(dict['userid'], dict['password'])
            dataformat = json.dumps(result)
            return jsonify(dataformat)
        except:
            return 'id not exits'


@app.route('/insertuserinfo', methods=['GET', 'POST'])
def insertuserinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        return SQLUtil.insertUserInfo(data)


@app.route('/getinfo', methods=['GET', 'POST'])
def getinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        result = SQLUtil.getInfo(data['id'], data['identity'])
        if reuslt == 0:
            return 0
        else:
            dataformat = json.dumps(result)
            return jsonify(dataformat)


@app.route('/getcourseinfo', methods=['GET', 'POST'])
def getcourseinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        result = SQLUtil.getCourseInfo(data['id'], data['identity'])
        if result == 0:
            return 0
        else:
            dataformat = json.dumps(result)
            return jsonify(dataformat)


@app.route('/getAttendanceInfo', method=['GET', 'POST'])
def getattendanceinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        result = SQLUtil.getAttendanceInfo(data['id'], data['identity'])
        if result == 0:
            return 0
        else:
            dataformat = json.dumps(result)
            return jsonify(dataformat)


@app.route('/addattendanceinfo', method=['GET', 'POST'])
def addattendanceinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        return  SQLUtil.addAttendanceInfo()


if __name__ == '__main__':
    app.run(debug=True)
