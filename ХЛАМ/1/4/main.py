import json

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/<title_name>')
@app.route('/index/<title_name>')
def index(title_name):
    return render_template('base.html', title=title_name)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')