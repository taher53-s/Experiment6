from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Name: John Doe</h1>
    <h2>AppID: APP-2024-001</h2>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
