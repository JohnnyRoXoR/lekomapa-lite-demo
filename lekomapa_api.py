from flask import Flask, request, jsonify
import pandas as pd


app = Flask(__name__)

# Load the medications dataset
DATA = pd.read_csv('medications.csv')


@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    if not query:
        return jsonify({'error': 'query parameter is required'}), 400
    results = DATA[DATA['name'].str.lower().str.contains(query)]
    return jsonify(results.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
