import mysql.connector


# 获取用户信息
def getUserinfo(userid, password):
    conn = mysql.connector.connect(user='root', password='', database='attendancedb')
    curor = conn.cursor()
    curor.execute('select * from user where id=%s'%userid)
    values = curor.fetchall()
    if values == []:
        return -1
    elif values[0][2] == password:
        if(values[0][1] == '学生'):
            curor.execute('select * from student where S_id=%s'%userid)
            values=curor.fetchall()
            res=(values[0][0], values[0][1], '学生', values[0][2], values[0][3])
            curor.close()
            return res
        elif(values[0][1] == '教师'):
            curor.execute('select * from teacher where T_id=%s'%userid)
            values=curor.fetchall()
            res=(values[0][0], values[0][1], '教师', values[0][2], values[0][3])
            curor.close()
            return res
    elif values[0][2] != password:
        curor.close()
        return 0


# 插入用户信息
def insertUserInfo(tuple):
    conn = mysql.connector.connect(user='root', password='', database='attendancedb')
    curor = conn.cursor()
    id = tuple[0]
    name = tuple[1]
    psw = tuple[2]
    identity = tuple[3]
    sex = tuple[4]
    collegeOrClass = tuple[5]
    curor.execute('select * from user where id=%s'%id)
    if curor.fetchall() != []:
        curor.close()
        return 0
    else:
        sql = 'insert into user values(%s,%s,%s)'
        l = (id, identity, psw)
        curor.execute(sql, l)
        conn.commit()
        if identity == '学生':
            sql = 'insert into student values(%s,%s,%s,%s)'
            l = (id, name, sex, collegeOrClass)
            curor.execute(sql, l)
            conn.commit()
            curor.close()
            return 1
        elif identity == '教师':
            sql = 'insert into teacher values(%s,%s,%s,%s)'
            l = (id, name, sex, collegeOrClass)
            curor.execute(sql, l)
            conn.commit()
            curor.close()
            return 1


# 修改用户信息
def updateUserInfo(tuple):
    conn = mysql.connector.connect(user='root', password='', database='attendancedb')
    curor = conn.cursor()
    id = tuple[0]
    name = tuple[1]
    psw = tuple[2]
    identity = tuple[3]
    sex = tuple[4]
    collegeOrClass = tuple[5]
    curor.execute('select * from user where id=%s'%id)

    if curor.fetchall() == []:
        curor.close()
        print('No such user')
        return 0
    elif identity == '学生':
        sql1 = 'update student set S_name=%s,Sex=%s,Major_class=%s where S_id=%s'
        sql2 = 'update user set identity=%s,u_password=%s where id=%s'
        l1 = (name, sex, collegeOrClass, id)
        l2 = (identity, psw, id)
        curor.execute(sql1, l1)
        curor.execute(sql2, l2)
        conn.commit()
        curor.close()
        return 1
    elif identity=='教师':
        sql1 = 'update teacher set T_name=%s,Sex=%s,College=% where T_id=%s'
        sql2 = 'update user set identity=%s,u_password=%s where id=%s'
        l1 = (name, sex, collegeOrClass, id)
        l2 = (identity, psw, id)
        curor.execute(sql1, l1)
        curor.execute(sql2, l2)
        conn.commit()
        curor.close()
        return 1
    else:
        return 0


# 获取教师和学生信息
def getInfo(id,identity):
    conn = mysql.connector.connect(user='root', password='', database='attendancedb')
    curor = conn.cursor()
    if identity == '学生':
        sql = 'select * from student where S_id=%s' % id
        curor.execute(sql)
        values=curor.fetchall()
        if values==[]:
            curor.close()
            return 0
        else:
            id=values[0][0]
            name=values[0][1]
            sex=values[0][2]
            c=values[0][3]
            curor.close()
            return (id,name,sex,c)
    elif identity=='教师':
        sql='select * from teacher where T_id=%s'%id
        curor.execute(sql)
        values=curor.fetchall()
        if values==[]:
            curor.close()
            return 0
        else:
            id=values[0][0]
            name=values[0][1]
            sex=values[0][2]
            c=values[0][3]
            curor.close()
            return (id,name,sex,c)


# 获取考勤情况
def getAttendanceInfo(id,identity):
    conn = mysql.connector.connect(user='root', password='', database='attendancedb')
    curor = conn.cursor()
    if identity=='课程':
        sql='select * from attend where courseid=%s'%id
        curor.execute(sql)
        values=curor.fetchall()
        if values==[]:
            curor.close()
            return 0
        else:
            res=[]
            for x in values:
                res.append((x[0],x[1],x[3],x[6]))
            curor.close()
            return res
    elif identity=='学生'or identity=='教师':
        sql = 'select * from attend where id=%s and identity=%s'
        l=(id,identity)
        curor.execute(sql,l)
        values = curor.fetchall()
        if values == []:
            curor.close()
            return 0
        else:
            res = []
            for x in values:
                res.append((x[5], x[3]))
            curor.close()
            return res


# 添加考勤情况
def addAttendanceInfo(info):
    if len(info)!=7:
        return -2
    conn = mysql.connector.connect(user='root', password='', database='attendancedb')
    curor = conn.cursor()
    sql='insert into attend values(%s,%s,%s,%s,%s,%s,%s)'
    l=(info[0],info[1],info[2],info[3],info[4],info[5],info[6])
    curor.execute(sql,l)
    conn.commit()
    curor.close()
    return 1

# 获取课程信息或课表
def getCourseInfo(id,identity):
    conn = mysql.connector.connect(user='root', password='', database='attendancedb')
    curor = conn.cursor()
    if identity=='课程':
        sql='select * from course where c_id=%s'%id
        curor.execute(sql)
        values=curor.fetchall()
        if values==[]:
            curor.close()
            return 0
        else:
            curor.close()
            return (values[0][0],values[0][1],values[0][2],values[0][3],values[0][4],values[0][5])
    elif identity=='教师':
        sql='select * from course where T_id=%s'%id
        curor.execute(sql)
        values=curor.fetchall()
        if values==[]:
            curor.close()
            return 0
        else:
            curor.close()
            return values
    elif identity=='学生':
        sql='select Major_class from student where S_id=%s'%id
        curor.execute(sql)
        values=curor.fetchall()
        if values==[]:
            return 0
        MajorClass=values[0][0]
        sql='select * from course where Major_class=%s'%"'"+MajorClass+"'"
        curor.execute(sql)
        values=curor.fetchall()
        if values==[]:
            return 0
        else:
            curor.close()
            return values





