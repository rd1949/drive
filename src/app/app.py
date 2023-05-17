import json

from flask import Blueprint, jsonify, request, redirect, send_file

from src.app.app_bo import APP_BO
app_bo = APP_BO()

users_blueprint = Blueprint('users', __name__, url_prefix='/users/api/v1')


@users_blueprint.route('/ping', methods=['GET'])
def index():
    agent = str(request.headers.get('User-Agent'))
    headers_list = request.headers.getlist("X-Forwarded-For")
    source_ip = headers_list[0] if headers_list else request.remote_addr
    return jsonify({'agent': str(agent), 'source_ip': str(source_ip), 'header': str(headers_list)})

@users_blueprint.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        data,html= app_bo.main(file=file)
        return send_file(data, download_name='data.xlsx', as_attachment=True)
    except Exception as ex:
        print(ex)
        return jsonify({'status': 'Fail!'})

@users_blueprint.route('/search', methods=['POST'])
def search():
    try:
        # data = json.loads(request.data)
        agent = str(request.headers.get('User-Agent'))
        headers_list = request.headers.getlist("X-Forwarded-For")
        source_ip = headers_list[0] if headers_list else request.remote_addr
        print(agent)
        print(source_ip)
        # domain = str(data['input']).strip()
        # response = app_bo.search(domain)
        return jsonify({'agent': str(agent),'source_ip': str(source_ip),'header': str(headers_list)})
    except Exception as ex:
        print(ex)
        return jsonify({'status': 'Fail!'})