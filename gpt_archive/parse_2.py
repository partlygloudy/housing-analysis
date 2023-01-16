import json
import sys

data = {}

with open(sys.argv[1], 'r') as f:
    key = None
    for line in f:
        if not line.startswith(','):
            key = line.strip()
            data[key] = {}
        else:
            line = line[1:]
            entries = line.strip().split(',')
            sub_key = entries[0]
            sub_data = entries[1:]
            data[key][sub_key] = sub_data

with open(sys.argv[2], 'w') as f:
    json.dump(data, f)