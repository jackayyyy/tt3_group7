from flask import Flask, request
import requests
import configparser


app = Flask(__name__)

def get_config():
    config = configparser.ConfigParser()
    config.read('flask.ini')
    xApiKey = config['DEFAULT']['x-api-key']
    return xApiKey


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/update')
def update():
    custID = request.args.get('custid', default='', type=str)
    amount = request.args.get('amount', default=0, type=int)
    return f"Trying to update {custID}'s balance to {amount}!"

@app.route('/login')
def login():
    global xApiKey
    base_url = r"https://849rs099m3.execute-api.ap-southeast-1.amazonaws.com/techtrek/login"
    username = request.args.get('username', default='', type=str)
    password = request.args.get('password', default='', type=str)
    
    headers = {
        "x-api-key": xApiKey
    }
    params = {
        "username": f"{username}",
        "password": f"{password}" 
    }
    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code != 200:
        return {
            "status_code": response.status_code,
            "response": response.text
        }
    else:
        return {
            "status_code": response.status_code,
            "response": response.text
        }

if __name__ == "__main__":
    xApiKey = get_config()
    app.run(debug=True)

# ngrok http 5000 (Command prompt, not git bash)

# sudo apt update && sudo apt upgrade -y
# sudo apt install python3
# sudo apt install python3-pip
# sudo pip install flask
# tmux new -s flaskapp
# CTRL+B, D
# flask run --host=0.0.0.0 --port=8080