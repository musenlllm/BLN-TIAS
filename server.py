# -*- coding: utf-8 -*-
from flask import Flask, jsonify,request,redirect,url_for
from flask_cors import CORS
from pymysql import connect
import pymysql
#import pandas as pd
from wordcloud import WordCloud
import json
app = Flask(__name__)
CORS(app)

TIME = ""
CAPTIME= ""
KEYWORD = ""
AUTHOR = ""
OPTION_LENGTH=[0,0,0,0,0]
Spider_list = [
    {
        "state":"关",
        "word":"台独",
        "len":"长",
        "address": "https://www.youtube.com"
    }, {
        "state":"关",
        "word":"膜",
        "len":"短",
        "address": "https://www.youtube.com"
    }
    , {
        "state":"开",
        "word":"蛤",
        "len":"中",
        "address": "https://www.youtube.com"
    }
]
'''
Database(MySQL): final

Table: websitelist
Columns: id, address, state, len, word

Table: video
Columns: 
'''
websitelist_sql ='''CREATE TABLE IF NOT EXISTS `websitelist`(
                       `id` INT UNSIGNED AUTO_INCREMENT,
                       `address` VARCHAR(100) NOT NULL,
                       `state` VARCHAR(40) NOT NULL,
                       `len` VARCHAR(40) NOT NULL,
                       `word` VARCHAR(40) NOT NULL,
                       PRIMARY KEY ( `id` )
                    )DEFAULT CHARSET=utf8;
                    '''
video_sql = '''CREATE TABLE IF NOT EXISTS `video`(
                       `id` INT UNSIGNED AUTO_INCREMENT,
                       `address` VARCHAR(100) NOT NULL,
                       `state` VARCHAR(40) NOT NULL,
                       `len` VARCHAR(40) NOT NULL,
                       `word` VARCHAR(40) NOT NULL,
                       PRIMARY KEY ( `id` )
                    )DEFAULT CHARSET=utf8;
                    '''

#连接数据库
def connect_mysql():
    try:
        conn = connect(host='localhost', port=3306, user='root', password='12345678', database='final', charset='utf8')
        cur = conn.cursor()
        return conn, cur
    except Exception as e:
        print(e)

# 创建数据库的表
def create_table(sql):
    try:
        conn, cur = connect_mysql()
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)

# 插入数据库
def insert_mysql(sql):
    try:
        conn, cur = connect_mysql()
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
#查询数据库
def find_mysql(sql):
    try:
        conn, cur = connect_mysql()
        cur.execute(sql)
        result = cur.fetchall()
        list = []
        for i in result:
            list.append(i)
        return list
    except Exception as e:
        print(e)

def selection_engine():
    global TIME,KEYWORD,AUTHOR,CAPTIME,OPTION_LENGTH
    if TIME !="":
        time_selection=" and substring(post_time,1,4)=\'%s\'" %TIME
    else:
        time_selection=""
    if KEYWORD !="":
        keyword_selection=' and v_name like "%'+KEYWORD+'%"'
    else:
        keyword_selection=""
    if AUTHOR !="":
        author_selection=' and post_author="'+AUTHOR+'"'
    else:
        author_selection=""
    if CAPTIME !="":
        captime_selection=" and substring(cap_time,1,10)=\'%s\'" %CAPTIME
    else:
        captime_selection=""

    video_selection_list=[]
    if OPTION_LENGTH[4] == 1:
        video_selection_5=" (length(v_time)>5)"
    else:
        video_selection_5=""
    if OPTION_LENGTH[3] == 1:
        video_selection_4=" (length(v_time)=5)"
    else:
        video_selection_4=""
    if OPTION_LENGTH[2] == 1:
        video_selection_3=" (length(v_time)=4 and convert(substring(v_time,1,1),SIGNED)>3)"
    else:
        video_selection_3=""
    if OPTION_LENGTH[1] == 1:
        video_selection_2=" (length(v_time)=4 and convert(substring(v_time,1,1),SIGNED)<4)"
    else:
        video_selection_2=""
    if OPTION_LENGTH[0]== 1:
        video_selection_1=" (length(v_time)=4 and convert(substring(v_time,1,1),signed)='0')"
    else:
        video_selection_1=""
    video_selection=""
    video_flag=1
    video_selection_list.append(video_selection_5)
    video_selection_list.append(video_selection_4)
    video_selection_list.append(video_selection_3)
    video_selection_list.append(video_selection_2)
    video_selection_list.append(video_selection_1)

    for video_item in video_selection_list:
        if video_item !="" and video_flag==1:
            video_flag=video_flag+1
            video_selection=video_selection+" and ("+ video_item
        if video_item !="" and video_flag!=1:
            video_selection=video_selection+" or"+ video_item
    if video_flag>1:
        video_selection=video_selection+" )"
    selection=time_selection+keyword_selection+author_selection+captime_selection+video_selection
    return selection

@app.route('/websitelist', methods=['GET'])
def weblist():
    sql = "select * from websitelist"
    result = find_mysql(sql)
    # print(result)
    payload = []
    content = {}
    for result in result:
        content = {'id': result[0], 'address': result[1]}
        payload.append(content)
        print(payload)
        content = {}
    return jsonify(payload)
    # return JSON.stringfy(payload)
 #（jsonify返回一个json格式的数据）

@app.route('/spiders', methods=['GET'])
def all_spiders():
    return jsonify({
        'status': 'success',
        'books': Spider_list
    })

@app.route('/upwebsitelist', methods=['POST'])
def upweblist():
    # 1.load url list filled in AdminBase.vue
    data = json.loads(request.get_data(as_text=True))

    # print("Data:",data,'\n',"Type of data:",type(data)) #list type

    # 2.delete old url list
    del_all = "DELETE FROM websitelist"
    insert_mysql(del_all)

    # 3.add new url list
    id =  0  #PRIMARY. # I don't know a better way to count. Perhaps use number of dict.
    for item in data:
        id += 1
        # print("Type of item:",type(item)) #dict type
        try:
            sql = "insert into websitelist values(\'%d\',\'%s\',\'%s\',\'%s\',\'%s\')" %(id,item['address'],item['state'],item['len'],item['word'])
            insert_mysql(sql)
        except Exception as e:
            print(e)
    return redirect(url_for("weblist"))

@app.route('/uptimeselect', methods=['POST'])
def uptimeselect():
    global TIME
    if request.get_data(as_text=True) == "":
        TIME=""
        print('1:uptimeselect')
    else:
        data = json.loads(request.get_data(as_text=True))
        print(str(int(data.split('-')[0])+1))
        TIME = str(int(data.split('-')[0])+1)
    return redirect(url_for("senslist"))

@app.route('/crawltimeselect', methods=['POST'])
def crawltimeselect():
    global CAPTIME
    if request.get_data(as_text=True) == "":
        CAPTIME=""
        print('2:crawltimeselect')
    else:
        data = request.get_data(as_text=True)
        print(data)
        CAPTIME = data
    return redirect(url_for("senslist"))

@app.route('/keywordselect', methods=['POST'])
def keywordselect():
    global KEYWORD
    if request.get_data(as_text=True) == "":
        KEYWORD=""
        print('333:keywordselect')
    else:
        data = request.get_data(as_text=True)
        print(data)
        KEYWORD = data
    return redirect(url_for("senslist"))

@app.route('/authorselect', methods=['POST'])
def authorselect():
    global AUTHOR
    if request.get_data(as_text=True) == "":
        AUTHOR=""
        print('444:authorselect')
    else:
        data = request.get_data(as_text=True)
        print(data)
        AUTHOR = data
    return redirect(url_for("senslist"))

@app.route('/leghthselect', methods=['POST'])
def leghthselect():
    global OPTION_LENGTH
    data = json.loads(request.get_data(as_text=True))
    print(data)
    OPTION_LENGTH = data.copy()
    print(OPTION_LENGTH)
    return redirect(url_for("senslist"))

@app.route('/baseshowlist', methods=['GET'])
def baselist():
    sql = "select * from video"
    result = find_mysql(sql)
    # print(result)
    payload = []
    content = {}
    for result in result:
        content = {'ID':result[0],'name': result[2], 'address': result[1],'time':result[4],'date':result[7],'download':result[10],'level':result[12],'detect':result[13]}
        payload.append(content)
        content = {}
    print("pay",payload)
    return jsonify(payload)

@app.route('/senslist', methods=['GET'])
def senslist():
    selection=selection_engine()
    sql_0="select v_level,count(*) from video where v_level=0"+selection
    sql_1="select v_level,count(*) from video where v_level=1"+selection
    sql_2="select v_level,count(*) from video where v_level=2"+selection
    sql_3="select v_level,count(*) from video where v_level=3"+selection
    sql_list=[sql_0,sql_1,sql_2,sql_3]
    # print("sql_list:",sql_list)
    payload = []
    content = {}
    for sql in sql_list:
        result = find_mysql(sql)
        # print("result:",result)
        if result[0][0]==0:
            slevel = "不敏感"
        elif result[0][0]==1:
            slevel = "低等敏感"
        elif result[0][0]==2:
            slevel = "中等敏感"
        else:
            slevel = "高等敏感"
        content = {'level':slevel,'num': result[0][1]}
        payload.append(content)
        content = {}
    # print(payload)
    return jsonify(payload)

@app.route('/posttimelist', methods=['GET'])
def posttimelist():
    selection=selection_engine()
    if selection == "":
        sql = "select substring(post_time,'1','4'),count(if(v_sensitive='1',true,null)),count(if(v_sensitive!='2',true,null)) from video group by substring(post_time,1,4) order by count(*) asc"
    else:
        sql = "select substring(post_time,'1','4'),count(if(v_sensitive='1',true,null)),count(if(v_sensitive!='2',true,null)) from video where 1=1"+selection+" group by substring(post_time,1,4) order by count(*) asc"
    result = find_mysql(sql)
    payload = []
    content = {}
    for result in result:
        content = {'post_time':result[0],'snum': result[1],'nnum': result[2]}
        payload.append(content)
        content = {}
    return jsonify(payload)

@app.route('/timelist', methods=['GET'])
def timelist():
    selection=selection_engine()
    sql_60="select '60-∞ minutes',count(if(v_sensitive=1,true,null)),count(if(v_sensitive!=2,true,null)) from video where length(v_time)>5"+selection
    sql_10_60="select '10-60 minutes',count(if(v_sensitive=1,true,null)),count(if(v_sensitive!=2,true,null)) from video where length(v_time)=5"+selection
    sql_4_10="select '4-10 minutes',count(if(v_sensitive=1,true,null)),count(if(v_sensitive!=2,true,null)) from video where length(v_time)=4 and convert(substring(v_time,1,1),SIGNED)<5 and convert(substring(v_time,1,1),SIGNED)>3"+selection
    sql_1_4="select '1-4 minutes',count(if(v_sensitive=1,true,null)),count(if(v_sensitive!=2,true,null)) from video where length(v_time)=4 and convert(substring(v_time,1,1),SIGNED)<4 and convert(substring(v_time,1,1),SIGNED)>1"+selection
    sql_0_1="select '0-1 minutes',count(if(v_sensitive=1,true,null)),count(if(v_sensitive!=2,true,null)) from video where length(v_time)=4 and convert(substring(v_time,1,1),signed)='0'"+selection
    sql_list=[sql_0_1,sql_1_4,sql_4_10,sql_10_60,sql_60]
    payload = []
    content = {}
    for sql in sql_list:
        result = find_mysql(sql)
        content = {'v_time':result[0][0],'snum': result[0][1],'nnum': result[0][2]}
        payload.append(content)
        content = {}
    return jsonify(payload)

@app.route('/themelist', methods=['GET'])
def themelist():
    sql = "select count(*) from key_word2"
    conn,cur = connect_mysql()
    number_of_key = cur.execute(sql)
    number_of_key=int(str(cur.fetchone()).replace("(","").replace(",)",""))
    payload = []
    content = {}
    for i in range(number_of_key):
        key_word=cur.execute("select w_word from key_word2 where w_id="+str(i+1))
        key_word=str(cur.fetchone()).replace("('","").replace("',)","")
        if key_word=="None":
            continue
        # print(key_word)
        selection=selection_engine()
        key_num = cur.execute("select count(*) from video where v_name like CONCAT(CONCAT('%',(select w_word from key_word where w_id="+str(i+1)+")),'%%')"+selection)
        # key_num = cur.execute("SELECT COUNT(*) FROM key_word")
        key_num= int(str(cur.fetchone()).replace("(","").replace(",)",""))
        print("key_num:",i,"+",key_num)
        content={'word':key_word,'count':key_num}
        payload.append(content)
    print(payload)
    return jsonify(payload)

@app.route('/sthemelist', methods=['GET'])
def sthemelist():
    global TIME
    sql = "select count(*) from key_word2"
    conn,cur = connect_mysql()
    number_of_key = cur.execute(sql)
    number_of_key=int(str(cur.fetchone()).replace("(","").replace(",)",""))
    payload = []
    content = {}
    for i in range(number_of_key):
        key_word=cur.execute("select w_word from key_word where w_id="+str(i+1))
        key_word=str(cur.fetchone()).replace("('","").replace("',)","")
        if key_word=="None":
            continue
        #print(key_word)
        selection=selection_engine()
        key_num = cur.execute("select count(*) from video where v_sensitive=1 and v_name like CONCAT(CONCAT('%',(select w_word from key_word where w_id="+str(i+1)+")),'%%')"+selection)
        key_num= int(str(cur.fetchone()).replace("(","").replace(",)",""))
        content={'word':key_word,'count':key_num}
        payload.append(content)
    return jsonify(payload)

@app.route('/authorlist', methods=['GET'])
def authorlist():
    selection=selection_engine()
    if selection=="":
        sql = "select post_author,count(*) from video group by post_author order by count(*) desc"
    else:
        sql = "select post_author,count(*) from video where 1=1"+selection+" group by post_author order by count(*) desc"
    result = find_mysql(sql)
    payload = []
    for result in result:
        content = {'word':result[0],'count': result[1]}
        payload.append(content)
        content = {}
    return jsonify(payload)

@app.route('/sauthorlist', methods=['GET'])
def sauthorlist():
    selection=selection_engine()
    if selection=="":
        sql = "select post_author,count(*) from video where v_sensitive=1 group by post_author order by count(*) desc"
    else:
        sql="select post_author,count(*) from video where v_sensitive=1"+selection+" group by post_author order by count(*) desc"
    result = find_mysql(sql)
    payload = []
    content = {}
    for result in result:
        content = {'word':result[0],'count': result[1]}
        payload.append(content)
        content = {}
    return jsonify(payload)

@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify ('hello world!')     #（jsonify返回一个json格式的数据）


if __name__ == '__main__':
    app.run()

