import json
with open('encrypt-decrypt.json', 'r') as arq:
    encrypt = json.load(arq)['encrypt']
   # decrypt = json.load(arq)['decrypt']

text = input("DIGITE O TEXTO: ")
mode = print("[1] Encrypt\n[2] Decrypt\n"), input("SELECIONE O MODO: ")

if mode[1] == '1' or mode[1] == '2' and text != "":
    if mode[1] == '1':
        counter = 0
        while counter < len(text):
            text = text.replace(text[counter], encrypt[text[counter]])
            counter = counter + 1
    if mode[1] == '2':
        counter = 0
        while counter < len(text):
            text = text.replace(text[counter], decrypt[text[counter]])
            counter = counter + 1
    print("OUTPUT: "+text)
else: 
    print("Erro: você não selecionou nenhum modo ou não digitou nenhum texto!!!")  






