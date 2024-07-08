import json
import os
from pathlib import Path

class Config:
    
    _attr = {}
    
    def __init__(self):
        config = load_definition()
        for attr in config.keys():
            self._attr[attr] = config[attr]
            pass
        pass
    
    def __str__(self):
        return str(self._attr)
    
    def __repr__(self):
        return str(self)
    
    def __getattr__(self,attr):
        if attr in self._attr.keys():
            return self._attr[attr]
        return None
    
    def __setattr__(self,attr,value):
        if value:
            self._attr[attr] = value
            pass
        pass
    
    pass

global config_file
config_file = 'HULK_DEFINITION'

def set_config_file_name(name):
    """
    change the name of the config file
    """
    global config_file
    config_file = name
    pass

def find_definition():
    global config_file
    """
    find the location of the language definition to tokenize
    """
    path = Path(os.getcwd())
    result = _find_definition(path)
    if result == None:
        raise Exception(f'the config file "{config_file}.json" does not exists on "{os.getcwd()}" path')
    return str(result)

def _find_definition(path):
    global config_file
    
    for file in path.iterdir():
        if file.is_file() and file.suffix == '.json' and file.name == config_file + '.json':
            return file
        pass
    for file in path.iterdir():
        if file.is_dir():
            result = _find_definition(path.joinpath(file.name))
            if result: return result
            pass
        pass
    return None

def load_definition():
    """
    loads the language definition to tokenize
    """
    path = find_definition()
    reader = open(path,'r')
    json_data = json.loads(reader.read())
    reader.close()
    return json_data

def GetConfig():
    """
    returns the language configuration
    """
    return Config()