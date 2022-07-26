import yaml
import json

## Create a variable to hold the data to import
os_list = {}

## Read the YAML file
with open("c:\temp\operating-systems.yml") as infile:
   with open("c:\temp\python_operating-systems.json", 'w') as outfile