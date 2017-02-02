__all__ = ['get_constant']

def get_constant_path(constant):
  import os
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  return os.path.join(BASE_DIR, "data", "constants", constant+".yaml")

def get_constant(constant):
  import yaml
  with open(get_constant_path(constant), 'r') as stream:
    data = yaml.load(stream)
    return data
