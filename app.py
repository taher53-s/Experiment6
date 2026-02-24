from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Name: Taher Sohagpurwala</h1>
    <h2>AppID: 2409540</h2>
    <h3>Hobbies:</h3>
    <ul>
        <li>Coding</li>
        <li>Reading</li>
        <li>Gaming</li>
    </ul>
    <br>
    <a href="/resume">View My Resume →</a>
    '''

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
