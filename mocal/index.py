from flask import render_template
from app import m_app

@m_app.route('/')
def hello_world():
    # return render_template('index.html', title='Mocal', name='Hi!Mocal.')
    return '1'

if __name__ == '__main__':
    m_app.run(debug=True, host='127.0.0.1', port=5000)
