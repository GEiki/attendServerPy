from flask import Flask
from flask import jsonify
from flask import request

import SQLUtil
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Attend'


@app.route('/getuserinfo', methods=['GET', 'POST'])
def getuserinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        result = SQLUtil.getUserinfo(data['userid'], data['password'])
        if result != 0 and result != 1:
            dataformat = json.dumps(result)
            return jsonify({'list': dataformat})
        else:
            return jsonify({'error': result})


@app.route('/insertuserinfo', methods=['GET', 'POST'])
def insertuserinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        return jsonify({'list':SQLUtil.insertUserInfo(data)})


@app.route('/getinfo', methods=['GET', 'POST'])
def getinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        result = SQLUtil.getInfo(data['id'], data['identity'])
        if result == 0:
            return jsonify({'result':result})
        else:
            dataformat = json.dumps(result)
            info = {'id': dataformat[0], 'name': dataformat[1], 'sex': dataformat[2], 'classorcollege': dataformat[3]}
            return jsonify({'list': info})


@app.route('/getcourseinfo', methods=['GET', 'POST'])
def getcourseinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        result = SQLUtil.getCourseInfo(data['id'], data['identity'])
        if result == 0:
            return jsonify({'error': 0})
        else:
            date = []
            samedate = []
            finaldata = {}
            for x in result:
                date.append(x[4].split())
            for y in date:
                if y[0] not in samedate:
                    samedate.append(y[0])
            for z in samedate:
                finaldata[z] = []
                for i in result:
                    tmp = i[4].split()
                    if tmp[0] == z:
                        finaldata[z].append(i)
            return jsonify({'list': finaldata})


@app.route('/getAttendanceInfo', methods=['GET', 'POST'])
def getattendanceinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        result = SQLUtil.getAttendanceInfo(data['id'], data['identity'])
        if result == 0:
            return jsonify({'error': 0})
        else:
            dataformat = json.dumps(result)
            return jsonify({'list': dataformat})


@app.route('/addattendanceinfo', methods=['GET', 'POST'])
def addattendanceinfo():
    if request.method == 'POST':
        d = request.get_data()
        data = json.loads(d)
        return jsonify({'error': SQLUtil.addAttendanceInfo(data[0], data[1])})

if __name__ == '__main__':
    debug=True
    app.run(host='0.0.0.0')
