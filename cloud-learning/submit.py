"""
The main point from this api is to submit a model in a `json` format and save into local files
## Rules 
1. model mush has a unique name 
"""

from flask import Blueprint, current_app, request, jsonify, abort
from .utils import raise_error, save_model_data
import os
import json

bp = Blueprint('submit', __name__, url_prefix='/submit')

required_keys = ['file', 'name']

@bp.route('/')
def submit_model():
    data = request.json

    if not data:
        error = "Can't Find `json` data in the request"
        return raise_error(error)
    missing_data = list()
    for key in required_keys:
        if key not in data.keys():
            missing_data.append(key)
    if missing_data:
        return raise_error(f'Missing Required Fields. {missing_data}')
    # Save the model into the `models` dir
    save_model_data(data)

    return jsonify({'ok': True})
