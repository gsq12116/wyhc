from flask import Blueprint, jsonify, request

from web.app.models import db

blue = Blueprint('goods', __name__)


@blue.route("/info/", methods=['get'])
def info():
    if request.method == 'get':
        pass