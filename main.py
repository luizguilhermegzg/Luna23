import json
with open('encrypt-decrypt.json', 'r') as arq_encrypt:
    encrypt = json.load(arq_encrypt)['encrypt']
with open('encrypt-decrypt.json', 'r') as arq_decrypt:
    decrypt = json.load(arq_decrypt)['decrypt']
text = input("DIGITE O TEXTO: ")
mode = print("[1] Encrypt\n[2] Decrypt\n"), input("SELECIONE O MODO: ")

if mode[1] == '1' or mode[1] == '2' and text != "":
    counter = 0
    output_text = ""
    if mode[1] == '1':
        while counter < len(text):
            output_text = output_text + encrypt[text[counter]]
            counter = counter + 1
    if mode[1] == '2':
        while counter < len(text):
            output_text = output_text + decrypt[text[counter]]
            counter = counter + 1
    print("OUTPUT: "+output_text)
else: 
    print("Erro: você não selecionou nenhum modo ou não digitou nenhum texto!!!")  






