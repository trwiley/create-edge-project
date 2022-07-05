import sys
import configparser
import json 

with open('sample_config_input.json', 'r') as config_input_file:
    config_data = config_input_file.read()

config_input = json.loads(config_data)

config = configparser.ConfigParser()
config.optionxform = str

config['project'] = {"cpu": 5,
        "projname": sys.argv[1][0:5],
        "projdesc": "",
        "projid": 8,
        "projcode": sys.argv[1],
        "projowner": "twiley1@nd.edu",
        "projrunhost": "http://localhost"}

for key in config_input:
    config[key] = config_input[key]

with open(f'{sys.argv[1]}/config.txt', 'w') as configfile:
    config.write(fileobject=configfile, space_around_delimiters=False)
