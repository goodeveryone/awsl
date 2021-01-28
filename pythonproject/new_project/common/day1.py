# !/usr/bin/env python
# -*- coding:utf-8 -*-



from flask import Flask,make_response,jsonify,abort,request

from flask import Flask,session
from werkzeug.security import safe_str_cmp
import json
import flask
from wsgiref.simple_server import make_server
# api = flask.Flask(__name__)
#
#
# @api.route('/login',methods=['get','post'])
# def aaa():
#     return "hello world"
#
# if __name__ == '__main__':
#    api.run(port=8888,debug=True,host='127.0.0.1') # 启动服务
#    debug=True  #,改了代码后，不用重启，它会自动重启
#



# def login():
#   #from-data格式参数
#   usrname = flask.request.values.get('usrname')
#   pwd = flask.request.values.get('pwd')
   
#   if usrname and pwd:
#     if usrname =='test' and pwd =='123456':
#       ren = {'msg':'登录成功','msg_code':200}
#     else:
#       ren = {'msg':'用户名或密码错误','msg_code':-1}
#   else:
#     ren = {'msg':'用户名或密码为空','msg_code':1001}
#   return json.dumps(ren,ensure_ascii=False)
 
# #post入参访问方式二：josn格式参数  
# @api.route('/loginjosn',methods=['post'])
# def loginjosn():
#   #from-data格式参数
#   usrname = flask.request.json.get('usrname')
#   pwd = flask.request.json.get('pwd')
   
#   if usrname and pwd:
#     if usrname =='test' and pwd =='123456':
#       ren = {'msg':'登录成功','msg_code':200}
#     else:
#       ren = {'msg':'用户名或密码错误','msg_code':-1}
#   else:
#     ren = {'msg':'用户名或密码为空','msg_code':1001}
#   return json.dumps(ren,ensure_ascii=False)
 
# if __name__ == '__main__':
#   api.run(port=8888,debug=True,host='127.0.0.1') # 启动服务
  # debug=True,改了代码后，不用重启，它会自动重启
  # 'host='127.0.0.1'别IP访问地址

#
new_name = ['博文']
dict = {'博文': '2005 all',}
# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'application/json')])
    # environ是当前请求的所有数据，包括Header和URL，body
    try:
        request_body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH", 0))).decode('utf-8')
        request_body = json.loads(request_body)
        name = request_body["name"]
        no = request_body["no"]
        if no == "123456" and name in new_name:
        # input your method here
        # for instance:
        # 增删改查
            dic = {'myNameIs': name,'resultcode':200,'身份证号':dict[name]}
            return [json.dumps(dic).encode('utf-8')]
        else:
            return ["请重新请求".encode('utf-8')]
    except:
        dic = "失败的人生不需要解释"
        return [dic.encode('utf-8')]

if __name__ == "__main__":
    port = 6088
    httpd = make_server("0.0.0.0", port, application)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()

# from flask import Flask,render_template,request
# app = Flask(__name__)
# print(app)
# @app.route("/login",methods = ['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         username = request.form.get('username')
#         password = request.form.get('password')
#         if username in ["zhangsan","lisi"] and password == "123":
#             return "Welcome %s" % username
#         else:
#             return "Login Failure!"
#     else:
#         return "Method Failure!"
#
# if __name__ == '__main__':
#     app.run('0.0.0.0',5000)
"""
import pymysql
import flask
import json
import tools
import hashlib

def add_res(username,password):
    conn = pymysql.connect(host='192.168.10.43', port=3306, user='root', passwd='123456',db='hhh')
    con = conn.cursor()
    con.execute(f'insert into register values("{username}","{password}");')
    conn.commit()
    conn.close()

def cha_res(*args):
    conn = pymysql.connect(host='192.168.10.43', port=3306, user='root', passwd='123456',db='hhh')
    con = conn.cursor()
    print(args)
    if len(args)==0:
        con.execute(f'select name from register;')
        name = [x[0] for x in con.fetchall()]
    elif len(args) ==  1:
        con.execute(f'select * from xinxi where id = {args[0]};')
        name = con.fetchall()
    elif len(args) == 2:
        con.execute(f'delete from xinxi where id = {int(args[-1])};')
        name = con.fetchall()
    else:
        con.execute(f'select * from register;')
        name = {x : y for x,y in con.fetchall()}
    conn.close()
    return name

server=flask.Flask(__name__)
@server.route('/register',methods=['post'])
def register():
    #登录需要两个参数，name和pwd
    uname=flask.request.values.get('username')# 传参，前面的是变量，括号里面是key
    passwd=flask.request.values.get('password')
    string = r"~!@#$%^&*()_+-*/<>,.[]\/"
    for i in string:
        if i in uname or i in passwd:
            res = {"error_code": 3001, "msg": "账号或密码无效！"}
            break
        if len(uname)<5 or len(uname)>12 or len(passwd)<5 or len(passwd)>12:
            res = {"error_code": 3001, "msg": "账号或密码无效！"}
            break
        if uname in cha_res():
            res = {"error_code": 3003, "msg": "账号已注册！"}
            break
    else:
            add_res(uname,passwd)
            res = {"error_code": 1000, "msg": "注册成功"}
    return json.dumps(res, ensure_ascii=False)

@server.route('/login',methods=['post'])
def login():
    #登录需要两个参数，name和pwd
    uname=flask.request.values.get('username')# 传参，前面的是变量，括号里面是key
    passwd=flask.request.values.get('password')
    asd = cha_res(123)
    #args只能获取到跟在url后面的参数，所以我们改用values
    try:
        if asd[uname]==passwd:# 非空为真
            res={"error_code":1000,"mag":"登录成功"}# 接口返回的都是json，所以要这样写。先导入json模块，import json。
    except:
            res = {"error_code": 3002, "mag": "账号或密码错误！"}

    return  json.dumps(res,ensure_ascii=False)#防止出现乱码；json.dumps()函数是将字典转化为字符串

@server.route('/add_student',methods=['post'])
def add_student():
    params=flask.request.json #入参是字典json时用它,下面的代码要判断传入的参数是否是json类型
    if params:
        name=params.get('name')
        sex=params.get('sex','男')# 如果没有传。默认值是男
        age=str(params.get('age'))# int
        phone=str(params.get('phone'))# 最少11位，不能重复
        if name and age and phone:# 必填参数校验
            if sex not in['男','女']: #如果性别不是男或者女
                res = {"error_code": 3003, "msg": "性别只能是男或者女"}
            elif not age.isdigit():# 如果不是整数类型
                res = {"error_code": 3004, "msg": "年龄输入错误"}
            elif len(phone)!=11 or not phone.isdigit():
                res = {"error_code": 3005, "msg": "手机号输入错误"}
            else:
                f = open('a.txt','r',encoding='utf-8')
                aa = f.readlines()
                phe=[]
                for i in aa:
                    i = i.split(',')
                    phe.append(i[-1])
                if phone in phe:
                    res = {"error_code": 1000, "msg": "手机号已经存在"}
                else:
                    f = open('a.txt','a',encoding='utf-8')
                    f.write(f'{name},{sex},{age},{phone}'+'\n')
                    f.close()
                    res = {"error_code": 200, "msg": "新增成功!"}
        else:
            res = {"error_code": 3007, "msg": "必填参数未填写"}
    else:
        res={"error_code":3002,"msg":"入参必须是json类型"}
    return  json.dumps(res,ensure_ascii=False)#防止出现乱码

@server.route('/delete',methods=['DELETE'])
def dele():
    uname = flask.request.values.get('id')
    cha_res(1,int(uname))
    if uname:
        res = {"error_code": 3000, "msg": "删除成功"}
    elif uname not in [1]:
        res = {"error_code": 3003, "msg": "删除失败"}
    else:
        res = {"err_code":3004,"msg":"错误的输入"}
    return json.dumps(res, ensure_ascii=False)


@server.route('/cha_xun/<int:id>',methods=['get'])
def cha(id):
    oo = []
    try:
        aa = cha_res(id)
        for i in aa:
            aaa = {'id': i[0], 'name': i[1], "phone": i[2]}
            oo.append(aaa)
        res = {"error_code": 3000, "msg": "查询成功", "result": oo}
    except:
        res = {"error_code": 3007, "msg": "查询失败"}

    return json.dumps(res, ensure_ascii=False)

if __name__ == '__main__':
    server.run(port=8880)
"""