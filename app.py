from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def ping():
    urls = request.json.get('urls', [])
    results = {}

    for url in urls:
        try:
            response = requests.get(url)
            results[url] = response.status_code == 200
        except requests.exceptions.RequestException as e:
            results[url] = False
    results ["status"]=200
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
