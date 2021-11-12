from sklearn.datasets import (
    load_boston, 
    load_breast_cancer, 
    load_diabetes, 
    load_digits, 
    load_iris, 
    load_wine, 
    load_files, 
    make_classification, 
    make_regression, 
    )

from tensorflow.keras.datasets import (
    mnist, 
    cifar10, 
    cifar100, 
    imdb, 
    boston_housing, 
    fashion_mnist
)

datasets = {
    'iris': 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv',
}


datasets_libs = {
    'sklearn': {
    'load_boston': load_boston, 
    'load_breast_cancer': load_breast_cancer, 
    'load_diabetes': load_diabetes, 
    'load_digits': load_digits, 
    'load_iris': load_iris, 
    'load_wine': load_wine, 
    'load_files': load_files, 
    'make_classification': make_classification, 
    'make_regression': make_regression, 
    }, 
    'keras': {
    'mnist': mnist, 
    'cifar10': cifar10, 
    'cifar100': cifar100, 
    'imdb': imdb, 
    'boston_housing': boston_housing, 
    'fashion_mnist': fashion_mnist
    }
}