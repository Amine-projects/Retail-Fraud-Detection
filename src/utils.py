import os

def make_dirs():
    if not os.path.exists('models'):
        os.makedirs('models')
