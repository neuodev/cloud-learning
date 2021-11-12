from flask import Response, current_app
import os
import json
from .datasets import datasets, datasets_libs
import requests


def raise_error(error, status=400):
    return Response(json.dumps({'error': error}), status=status, mimetype='application/json')

def save_model_data(data):
    models_dir = os.path.join(current_app.instance_path, 'models')
    if not os.path.exists(models_dir):
        os.mkdir(models_dir)
    # Model should not be saved twice unless it forced 
    if not data.get('force', None):
        for model in os.listdir(models_dir):
            if model == data['name']:
                return raise_error(f'`{data["name"]}` Model Already Exist')
    # Create new model dir 
    new_model_path = os.path.join(models_dir, data['name'])
    if not os.path.exists(new_model_path):
        os.mkdir(new_model_path)
    # Save the model in the json format 
    model_py_path = os.path.join(new_model_path, f'{data["name"]}.py')
    with open(model_py_path, 'w') as f:
        f.write(data['file'])


def load_model_data(name):
    # Check if the model exist
    model_path = os.path.join(current_app.instance_path, 'models', f'{name}.json')
    if not os.path.exists(model_path):
        return 
    # Read the file 
    with open(model_path, 'r') as f:
        data = json.loads(f.read())
    
    return data

def load_dataset_from_dir(name: str):
    if name.startswith('sklearn'):
        dataset = name.split('/')[1]
        sklearn_ds = datasets_libs['sklearn']
        if dataset not in sklearn_ds.keys():
            return
        X_train, y_train = sklearn_ds[dataset](return_X_y=True)
        return X_train, y_train

    if name.startswith('keras'):
        dataset = name.split('/')[1]
        keras_ds = datasets_libs['keras']
        if dataset not in keras_ds.keys():
            return
        return keras_ds[dataset].load_data()
    # Check if the dir exist 
    datasets_dir = os.path.join(current_app.instance_path, 'datasets')
    if not os.path.exists(datasets_dir):
        print('Datasets directory doesn\'t exist\nneed to run `flask install datasets` first')
        return 

def load_datasets_from_remote():
    datasets_dir = os.path.join(current_app.instance_path, 'datasets')
    if not os.path.exists(datasets_dir):
        os.mkdir(datasets_dir)
    
    existed_datasets = os.listdir(datasets_dir)
    existed_datasets = [x.split('.')[0] for x in existed_datasets]
    for name, url in datasets.items():
        if name not in existed_datasets:
            # Create new file
            new_datset_file = os.path.join(datasets_dir, f"{name}.csv")
            # Get the data from the url
            res = requests.get(url).text
            with open(new_datset_file, 'w') as f:
                f.write(res)
        else:
            print(f'{name} already exist!!')



