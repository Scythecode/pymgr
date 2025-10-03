import configparser,json
from sys import argv
confparser = configparser.ConfigParser()
my_config = None
with open("config.json","r") as f:
    my_config = json.load(f)

def initodict(ini):
    # Totally not stolen from https://www.pythonforbeginners.com/basics/convert-ini-files-to-json-format-in-python
    config_object = configparser.ConfigParser()
    file =open(ini,"r")
    config_object.read_file(file)
    output_dict=dict()
    sections=config_object.sections()
    for section in sections:
        items=config_object.items(section)
        output_dict[section]=dict(items)
    file.close()
    return output_dict
if type(my_config["repositories"]) is str: my_config["repositories"] = initodict(my_config["repositories"])