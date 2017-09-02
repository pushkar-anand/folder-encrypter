import json

with open('folder.json') as data_file:
    data = json.load(data_file)
folders = data["folders"]

