"""
The main point from this api is to submit a model in a `json` format and save into local files
## Rules 
1. model mush has a unique name 
"""

from flask import Blueprint, current_app, request, jsonify, abort
from .utils import rise_error
import os
import json

bp = Blueprint('submit', __name__, url_prefix='/submit')

required_keys = ['model', 'opt', 'loss', 'name']

@bp.route('/')
def submit_model():
    data = request.json

    if not data:
        error = "Can't Find `json` data in the request"
        return rise_error(error)
    missing_data = list()
    for key in required_keys:
        if key not in data.keys():
            missing_data.append(key)
    if missing_data:
        return rise_error(f'Missing Required Fields. {missing_data}')
    # Save the model into the `models` dir
    models_dir = os.path.join(current_app.instance_path, 'models')
    if not os.path.exists(models_dir):
        os.mkdir(models_dir)
    # Model should not be saved twice 
    for model in os.listdir(models_dir):
        if model == data['name']:
            return rise_error(f'`{data["name"]}` Model Already Exist')
    # Create new model dir 
    new_model_path = os.path.join(models_dir, data['name'])
    os.mkdir(new_model_path)
    # Save the model in the json format 
    model_json_path = os.path.join(new_model_path, f'{data["name"]}.json')
    with open(model_json_path, 'w') as f:
        f.write(json.dumps({
            'model': data['model'], 
            'meta': {
                'loss': data['loss'], 
                'opt': data['opt'], 
                'name': data['name']
            }
        }))
        
    return jsonify({'ok': 'ok'})
    