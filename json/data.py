import json

data = {
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}

with open('data_file.json', 'w') as f:
    json.dump(data, f)

with open("data_file.json", "r") as fh:
    json.load(fh)
    print(json.dump(fh))
