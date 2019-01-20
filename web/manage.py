from flask import Flask, render_template, jsonify

from web.app.models import Good, db
from web.setting import DATABASES


app = Flask(__name__)

# 密钥配置
app.config['SECRET_KEY'] = '123'
app.config['JSON_AS_ASCII'] = False

# 数据库配置
default_database = DATABASES['default']
app.config['SQLALCHEMY_DATABASE_URI'] = '{}+{}://{}:{}@{}:{}/{}'.format(default_database['DRIVER'],
                                                                        default_database['DH'],
                                                                        default_database['USER'],
                                                                        default_database['PASSWORD'],
                                                                        default_database['HOST'],
                                                                        default_database['PORT'],
                                                                        default_database['NAME'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/info/')
def info():
    goods_info = []
    goods = Good.query.all()
    for good in goods:
        goods_info.append(good.to_dict())
    return jsonify(goods_info=goods_info)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)