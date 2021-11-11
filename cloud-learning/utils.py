from flask import jsonify, Response
import json

def rise_error(error, status=400):
    return Response(json.dumps({'error': error}), status=status, mimetype='application/json')