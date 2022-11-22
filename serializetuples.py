# Stack Overflow Post: https://stackoverflow.com/questions/7001606/json-serialize-a-dictionary-with-tuples-as-key

def json_dumps_tuple_keys(mapping):
    string_keys = {json.dumps(k): v for k, v in mapping.items()}
    return json.dumps(string_keys)

def json_loads_tuple_keys(string):
    mapping = json.loads(string)
    return {tuple(json.loads(k)): v for k, v in mapping.items()}