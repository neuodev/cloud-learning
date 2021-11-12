from flask import Blueprint, current_app, request, send_file, send_from_directory
import os
from .utils import raise_error

from flask.json import jsonify 

bp = Blueprint('download', __name__, url_prefix='/download')

types = ['models', 'datasets', 'all']

@bp.route('/arch/<string:type>')
def download_arch(type):
    if type not in types:
        return raise_error(f'`type` should be one of {types}')
    path = os.path.join(current_app.instance_path)
    if type == 'models':
        path = os.path.join(path, 'models')
    elif type == 'datasets':
        path = os.path.join(path, 'datasets')
    
    dirs = os.walk(path)
    data = dict()
    for root, subdirs, files in dirs:
        root = root.split('/')
        root = root[len(root) - 1]
        data[root] = {
            'subdirs': subdirs, 
            'files': files, 
        }
    
    return jsonify(data)

@bp.route('/')
def download():
    path = request.args.get('path', None)
    if not path:
        return raise_error('Missing required filed `path`')
    file_path = os.path.join(current_app.instance_path, path)
    if not os.path.exists(file_path):
        return raise_error(f"{file_path} doesn't exist!!")
    if os.path.isdir(file_path):
        return raise_error("Path should be file not a directory")
    return send_file(file_path, download_name='model.py')
    
