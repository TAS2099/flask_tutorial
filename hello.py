from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/goodbye')
def goodbye():
    return 'goodbye!'

if __name__=='__main__':
    app.run(port=5001, host='0.0.0.0')