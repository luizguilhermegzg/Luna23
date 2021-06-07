with open('encrypt-decrypt.json') as f:
    keys_encrypt = json.load(encrypt, f)
print(keys_encrypt['a'])