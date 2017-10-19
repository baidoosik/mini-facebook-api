from ...api_1 import api_1
from ..user.models import User
from flask import url_for, jsonify


@api_1.route('/user/<int:id>/', methods=['GET'])
def user_detail(id):
    return jsonify({
        'user':User.query.filter_by(id=id).first().to_json()
    })


@api_1.route('/user/list/', methods=['GET'])
def user_list():
    return jsonify({
        'user_list':[u.to_json() for u in User.query.all()]
    })