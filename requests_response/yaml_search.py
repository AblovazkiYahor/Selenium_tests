import yaml
from pprint import pprint

with open('order.yaml') as f:
    templates = yaml.safe_load(f)

pprint(templates)