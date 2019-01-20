from flask import Flask, render_template

from web.app.views import blue

app = Flask(__name__)

app.config['SECRET_KEY'] = '123'
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(blue, url_prefix='/goods')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)