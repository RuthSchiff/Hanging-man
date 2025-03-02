import json
from itertools import count
import sys
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
import random
import os

from select import error

basic_url = "http://127.0.0.1:5000"
data_file = "../Data.txt"

players_data = {}
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/set_cookie', methods=['POST'])
def set_cookie_func():
    obj = request.json
    response = make_response("Cookie set!")
    response.set_cookie("user", obj['user_name'], max_age=600, httponly=True, secure=False, samesite='None')
    return response

@app.route('/get_cookie', methods=['GET'])
def get_cookie_func():
    user_name = request.cookies.get('user')
    if user_name:
        return make_response("Cookie found!"),200
    return make_response("Cookie not found"),404


# קבלת מילה
@app.route('/get_word', methods=['GET'])
def get_word():
    with open("../game'sWords.txt", 'r') as file:
        words = file.read().split(',')
    return jsonify(words)

# # קריאת הנתונים
def find_players():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            content = file.read()
            if content.strip():
                try:
                    return json.loads(content)
                except json.JSONDecodeError:
                    print("Error: Data file is not in valid JSON format.")
                    return {}
    return {}


# כתיבת שחקנים
def write_players(players_data):
    with open(data_file, 'w') as file_w:
        json.dump(players_data, file_w)
        file_w.close()

# התחברות
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')

    # בדיקה האם הלקוח קיים
    if name in players_data and players_data[name]['password'] == password:
        return jsonify({"status": "exist"}), 200
        return data.get("name")
    else:
        return jsonify({"status": "not found", }), 404


# הרשמה
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get("name")
    id_number = data.get("id_number")
    password = data.get("password")
    count_games = data.get("count_games", 0)
    words = data.get("words", {})
    count_winner = data.get("count_winner", 0)

    if name not in players_data:
        players_data[name] = {
            "id_number": id_number,
            "password": password,
            "count_games": count_games,
            "words": words,
            "count_winner": count_winner,
        }
        write_players(players_data)
        return jsonify({"status": "registered"}), 201
    return jsonify({"status": "already exist"}), 409



@app.route('/add_winner', methods=['POST'])
def add_winner():
    players = find_players()
    if not players:
        print("Error: No players found.")
        return jsonify({"status": "no players found"}), 500

    data = request.get_json()
    name = data.get("name")
    password = data.get("password")

    for player_name, player_data in players.items():
        if player_name == name and player_data['password'] == password:
            player_data['count_winner'] = int(player_data['count_winner']) + 1

            with open(data_file, 'w') as fwi:
                json.dump(players, fwi)

            return jsonify({"status": "winner updated"}), 200

    return jsonify({"status": "player not found"}), 404


@app.route('/add_game', methods=['POST'])
def add_game():
    try:
        data = request.json
        print(f"Received data: {data}")  # הדפסת הנתונים המתקבלים

        name = data.get("name")
        password = data.get("password")

        players = find_players()
        if not players:
            print("Error: No players found.")
            return jsonify({"status": "no players found"}), 500

        for player_name, player_data in players.items():
            if player_name == name and player_data['password'] == password:
                player_data['count_games'] = int(player_data['count_games'])+1
                break
        else:
            return jsonify({"status": "not found"}), 404


        with open(data_file, 'w') as fw:
            json.dump(players, fw)

        return jsonify({"status": "exist"}), 200

    except:
        e = sys.exc_info()[0]
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/add_word', methods=['POST'])
def add_word():
        data = request.json
        name = data.get("name")
        password = data.get("password")
        word = data.get("word")

        players = find_players()
        if not players:
            return jsonify({"status": "not found"}), 404

        for player_name, player_data in players.items():
            if player_name == name and player_data['password'] == password:
                if word not in player_data['words']:
                    player_data['words'].append(word)
                    write_players(players)
                    return jsonify({"status": "word added"}), 200

                else:
                    return jsonify({"status": "word already exists"}), 409

        return jsonify({"status": "player not found"}), 404


@app.route('/get_history', methods=['POST'])
def get_history():
        data = request.json
        name = data.get("name")
        password = data.get("password")

        players = find_players()

        if not players:
            return jsonify({"status": "not found"}), 404

        for player_name, player_data in players.items():
            if player_name == name and player_data['password'] == password:

                return jsonify({

                    "count_games": player_data['count_games'],
                    "count_winner": player_data['count_winner'],
                    "words": player_data['words']
                }), 200
        return jsonify({"status": "word already exists"}), 409



if __name__ == '__main__':

    players_data = find_players()

    app.run(debug=True, port=5000)
