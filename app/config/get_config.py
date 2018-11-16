import os

import yaml


def get_config():
    path = os.path.join('app', 'config', 'config.yml')
    with open(path, 'r') as file:
        config = yaml.load(file)
    return config
