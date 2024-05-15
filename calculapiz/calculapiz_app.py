"""Entry point of application. Here specified some routes and blueprint s imports"""
from flask import Flask, send_file, redirect

from app.config import DATA_PATH


app = Flask(__name__)

from app.operations import bp as operations_bp

app.register_blueprint(operations_bp, url_prefix='/api/v1')


@app.route('/')
def main():
    return redirect('/about', code=302)


@app.route('/about/')
def about():
    return send_file('app/templates/about.html')


if __name__ == '__main__':
    import os
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)

    port = 5000
    app.run(debug=False, port=port, host='0.0.0.0')
