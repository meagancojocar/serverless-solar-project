# Required imports
from flask import Flask, jsonify, request

app = Flask(__name__)

readings = [
    {'timestamp': 1,
     'import': 1,
     'export': 1},
    {'timestamp': 2,
     'import': 2,
     'export': 2},
]


@app.route('/readings', methods=['GET'])
def get_readings():
    return jsonify(readings)

@app.route('/readings', methods=['POST'])
def get_readings():
    pass

if __name__ == '__main__':
    app.run(debug=True)
