import sys
import configparser
import json 

with open('sample_config_input.json', 'r') as config_input_file:
    config_data = config_input_file.read()

config_input = json.loads(config_data)

config = configparser.ConfigParser()

for key in config_input:
    config[key] = config_input[key]
    
with open('config.txt', 'w') as configfile:
    config.write(configfile)
