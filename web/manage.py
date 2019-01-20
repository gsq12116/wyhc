from flask import Flask, render_template

from web.app.views import blue
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

# 蓝图绑定
app.register_blueprint(blueprint=blue, url_prefix='/goods')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)