import json
# Import a json file with all characters replacements.
with open('./json/encrypt-decrypt.json', 'r') as arq_encrypt:
    encrypt = json.load(arq_encrypt)['encrypt']
with open('./json/encrypt-decrypt.json', 'r') as arq_decrypt:
    decrypt = json.load(arq_decrypt)['decrypt']

# Ask to input an text and mode of the replacement.
def settings():
    text = input("\nDIGITE O TEXTO: ")
    mode = print("[1] Encrypt\n[2] Decrypt\n"), input("SELECIONE O MODO: ")
    encrypt_decrypt(text, mode)

# Finally here the text inserted is replaced by the characters of luna23.
def encrypt_decrypt(inserted, mode_select): 
    if mode_select[1] == '1' or mode_select[1] == '2' and inserted != "":
        i = 0
        output_text = ""
        if mode_select[1] == '1':
            while i < len(inserted):
                output_text = output_text + encrypt[inserted[i]]
                i += 1
        if mode_select[1] == '2':
            while i < len(inserted):
                output_text = output_text + decrypt[inserted[i]]
                i += 1
        print("OUTPUT: "+output_text)
    else: 
        print("Erro: você não selecionou nenhum modo ou não digitou nenhum texto!!!")

# Execute the initial function settings after encrypt_decrypt() function be defined.
settings()

