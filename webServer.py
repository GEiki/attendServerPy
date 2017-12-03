from flask import Flask
from flask import jsonify
from flask import request

import SQLUtil
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'attendServer'


@app.route('/getuserinfo', methods=['GET', 'POST'])
def getuserinfo():
    if request.method == 'POST':
        d = request.get_data().decode('utf-8')
        data = json.loads(d)
        result = SQLUtil.getUserinfo(data['userid'], data['password'])
        if result != 0 and result != 1:
            tmp = [result[0],
                   result[1],
                   result[2],
                   result[3],
                   result[4]]
            return jsonify({'list': tmp})
        else:
            return jsonify({'error': result})


@app.route('/insertuserinfo', methods=['GET', 'POST'])
def insertuserinfo():
    if request.method == 'POST':
        d = request.get_data().decode('utf-8')
        data = json.loads(d)
        tmp = (data['id'], data['username'],
               data['password'],
               data['identity'],
               data['sex'],
               data['collegeOrClass'])
        return jsonify({'result': SQLUtil.insertUserInfo(tmp)})


@app.route('/getinfo', methods=['GET', 'POST'])
def getinfo():
    if request.method == 'POST':
        d = request.get_data().decode('utf-8')
        data = json.loads(d)
        result = SQLUtil.getInfo(data['id'], data['identity'])
        if result == 0:
            return jsonify({'result': result})
        else:
            info = {'id': result[0],
                    'name': result[1],
                    'sex': result[2],
                    'classorcollege': result[3]}
            dataformat = json.dumps(info)
            return jsonify({'list': dataformat})


@app.route('/getcourseinfo', methods=['GET', 'POST'])
def getcourseinfo():
    if request.method == 'POST':
        d = request.get_data().decode('utf-8')
        data = json.loads(d)
        result = SQLUtil.getCourseInfo(data['id'], data['identity'])
        if result == 0:
            return jsonify({'error': 0})
        else:
            date = []
            samedate = []
            finaldata = {}
            for x in result:
                date.append(x[4].strftime("%Y-%m-%d %H:%M:%S").split())
            for y in date:
                if y[0] not in samedate:
                    samedate.append(y[0])
            for z in samedate:
                finaldata[z] = []
                for i in result:
                    tmp = i[4].strftime("%Y-%m-%d %H:%M:%S").split()
                    if tmp[0] == z:
                        end = list(i)
                        end[4] = "%s年%s月%s日 %s:%s:%s" % (i[4].year,
                                                         i[4].month,
                                                         i[4].day,
                                                         i[4].hour,
                                                         i[4].minute,
                                                         i[4].second)
                        finaldata[z].append(end)
            return jsonify({'list': finaldata})


@app.route('/updateuserinfo', methods=['GET', 'POST'])
def updateuserinfo():
    if request.method == 'POST':
        d = request.get_data().decode('utf-8')
        data = json.loads(d)
        result = SQLUtil.updateUserInfo((data['id'],
                                         data['username'],
                                         data['password'],
                                         data['identity'],
                                         data['sex'],
                                         data['collegeOrClass']))
        return jsonify({'error': result})


@app.route('/getattendanceinfo', methods=['GET', 'POST'])
def getattendanceinfo():
    if request.method == 'POST':
        d = request.get_data().decode('utf-8')
        data = json.loads(d)
        result = SQLUtil.getAttendanceInfo(data['id'], data['identity'])
        if result == 0:
            return jsonify({'error': 0})
        else:
            if data['identity'] == '课程':
                tmp = [{'id': x[0], 'name': x[1], 'attend': x[2], 'position': x[3]} for x in result]
            else:
                tmp = [{'course': x[0], 'attend':x[1]} for x in result]
            return jsonify({'list': tmp})


@app.route('/addattendanceinfo', methods=['GET', 'POST'])
def addattendanceinfo():
    if request.method == 'POST':
        d = request.get_data().decode('utf-8')
        info = json.loads(d)
        tmp = (info['id'],
               info['name'],
               info['identity'],
               info['attend'],
               info['courseid'],
               info['coursename'],
               info['position'])
        result = SQLUtil.addAttendanceInfo(tmp)
        return jsonify({'error': result})

if __name__ == '__main__':
    debug = True
    app.run(host='0.0.0.0')
