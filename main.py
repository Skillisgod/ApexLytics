from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

API_KEY = "" 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classe')
def classe():
    return render_template('ranked.html')

@app.route('/classement')
def classement():
    return render_template('predator.html')

@app.route('/stats', methods=['GET'])
def stats_page():
    return render_template('stats.html')

@app.route('/api/stats', methods=['GET'])
def get_stats():
    player = request.args.get('player')
    platform = request.args.get('platform', 'PC')

    if not player:
        return jsonify({"error": "Veuillez fournir un nom de joueur"}), 400

    url = f"https://api.mozambiquehe.re/bridge?auth={API_KEY}&player={player}&platform={platform}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Impossible de récupérer les données"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5001)
