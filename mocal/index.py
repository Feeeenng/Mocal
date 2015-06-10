from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', title='Hello World!', name='haner27!')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
