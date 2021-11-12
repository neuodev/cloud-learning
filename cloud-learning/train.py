from .utils import load_model_data

def train_model(name):
    # Load the model
    data = load_model_data()

    if not data:
        return print('Model not Found')
    
    # Load Model data 
    

