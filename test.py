import json
with open('encrypt-decrypt.json', 'r') as arq:
    obj = json.load(arq)['encrypt']
print(obj['a'])
