from flask import Flask, request, send_from_directory, jsonify
import csv
import os

app = Flask(__name__)

@app.route('/')
def login():
    return send_from_directory('.', 'login.html')

@app.route('/data.csv')
def get_csv():
    return send_from_directory('.', 'data.csv')

@app.route('/sport')
def sport():
    return send_from_directory('.', 'sport.html')

@app.route('/dati')
def dati():
    return send_from_directory('.', 'dati.html')

@app.route('/map_demo')
def map_demo():
    return send_from_directory('.', 'map_demo.html')

@app.route('/home')
def home():
    return send_from_directory('.', 'home.html')
@app.route('/homeen')
def homeen():
    return send_from_directory('.', 'homeen.html')
@app.route('/homede')
def homede():
    return send_from_directory('.', 'homede.html')
@app.route('/homefr')
def homefr():
    return send_from_directory('.', 'homefr.html')
@app.route('/homees')
def homees():
    return send_from_directory('.', 'homees.html')
@app.route('/homeja')
def homeja():
    return send_from_directory('.', 'homeja.html')
@app.route('/homeko')
def homeko():
    return send_from_directory('.', 'homeko.html')
@app.route('/homeru')
def homeru():
    return send_from_directory('.', 'homeru.html')

@app.route('/jiankangpao')
def jiankangpao():
    return send_from_directory('.', 'jiankangpao.html')
@app.route('/jiankangpaoen')
def jiankangpaoen():
    return send_from_directory('.', 'jiankangpaoen.html')
@app.route('/jiankangpaode')
def jiankangpaode():
    return send_from_directory('.', 'jiankangpaode.html')
@app.route('/jiankangpaofr')
def jiankangpaofr():
    return send_from_directory('.', 'jiankangpaofr.html')
@app.route('/jiankangpaoes')
def jiankangpaoes():
    return send_from_directory('.', 'jiankangpaoes.html')
@app.route('/jiankangpaoja')
def jiankangpaoja():
    return send_from_directory('.', 'jiankangpaoja.html')
@app.route('/jiankangpaoko')
def jiankangpaoko():
    return send_from_directory('.', 'jiankangpaoko.html')
@app.route('/jiankangpaoru')
def jiankangpaoru():
    return send_from_directory('.', 'jiankangpaoru.html')

@app.route('/yuanxifootball')
def yuanxifootball():
    return send_from_directory('.', 'yuanxifootball.html')
@app.route('/yuanxifootballru')
def yuanxifootballru():
    return send_from_directory('.', 'yuanxifootballru.html')
@app.route('/yuanxifootballde')
def yuanxifootballde():
    return send_from_directory('.', 'yuanxifootballde.html')
@app.route('/yuanxifootballko')
def yuanxifootballko():
    return send_from_directory('.', 'yuanxifootballko.html')
@app.route('/yuanxifootballja')
def yuanxifootballja():
    return send_from_directory('.', 'yuanxifootballja.html')
@app.route('/yuanxifootballen')
def yuanxifootballen():
    return send_from_directory('.', 'yuanxifootballen.html')
@app.route('/yuanxifootballfr')
def yuanxifootballfr():
    return send_from_directory('.', 'yuanxifootballfr.html')
@app.route('/yuanxifootballes')
def yuanxifootballes():
    return send_from_directory('.', 'yuanxifootballes.html')

@app.route('/lalacao')
def lalacao():
    return send_from_directory('.', 'lalacao.html')
@app.route('/lalacaoru')
def lalacaoru():
    return send_from_directory('.', 'lalacaoru.html')
@app.route('/lalacaode')
def lalacaode():
    return send_from_directory('.', 'lalacaode.html')
@app.route('/lalacaoko')
def lalacaoko():
    return send_from_directory('.', 'lalacaoko.html')
@app.route('/lalacaoja')
def lalacaoja():
    return send_from_directory('.', 'lalacaoja.html')
@app.route('/lalacaoen')
def lalacaoen():
    return send_from_directory('.', 'lalacaoen.html')
@app.route('/lalacaofr')
def lalacaofr():
    return send_from_directory('.', 'lalacaofr.html')
@app.route('/lalacaoes')
def lalacaoes():
    return send_from_directory('.', 'lalacaoes.html')

@app.route('/update', methods=['POST'])
def update_csv():
    user_id = request.json['userId']
    
    # 读取CSV文件
    rows = []
    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # 查找并更新用户数据
    updated = False
    for row in rows:
        if row[0] == user_id:
            # 倒数第二列加1
            row[-2] = str(int(row[-2]) + 1)
            updated = True
            break
    
    if updated:
        # 写回CSV文件
        with open('data.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        return {'status': 'success'}, 200
    else:
        return {'status': 'user not found'}, 404
    
@app.route('/growtree')
def growtree():
    return send_from_directory('.', 'growtree.html')
    
@app.route('/get_user_data', methods=['GET'])
def get_user_data():
    user_id = request.args.get('id')
    if not user_id:
        return jsonify({'status': 'error', 'message': 'User ID is required'}), 400

    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == user_id:
                return jsonify({
                    'id': row[0],
                    'name': row[1],
                    'credit': int(row[3]),
                    'activity': int(row[4])
                })
    return jsonify({'status': 'error', 'message': 'User not found'}), 404

# 新增路由：更新用户积分
@app.route('/update_credit', methods=['POST'])
def update_credit():
    user_id = request.json.get('userId')
    if not user_id:
        return jsonify({'status': 'error', 'message': 'User ID is required'}), 400

    rows = []
    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    updated = False
    for row in rows:
        if row[0] == user_id:
            row[3] = str(int(row[3]) + 5)  # 更新积分
            row[4] = str(int(row[4]) - 1)
            updated = True
            break

    if updated:
        with open('data.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        return jsonify({'status': 'success', 'newCredit': int(row[3])})
    else:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404
    
@app.route('/map')
def map():
    return send_from_directory('.', 'map.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)  # 关闭 debug 模式
