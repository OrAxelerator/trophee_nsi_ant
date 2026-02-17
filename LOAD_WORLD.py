import json


def load_project(name):
    with open(f'WORLD/{name}.json') as f:
        d = json.load(f)
    map = []
    map.append(d[name])
    return map[0]
