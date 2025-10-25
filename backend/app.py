from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/health')
def health():
    return jsonify({"status":"ok"})

@app.route('/api/products')
def products():
    return jsonify([{"id":1,"name":"Pen"},{"id":2,"name":"Notebook"}])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
