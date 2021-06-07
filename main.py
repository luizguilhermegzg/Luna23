text = input("DIGITE O TEXTO: ")

mode = print("[1] Encrypt\n[2] Decrypt\n"), input("SELECIONE O MODO: ")


if mode[1] == '1' or mode[1] == '2':
    if mode[1] == '1':
        counter = 0
        while counter < len(text):
            text = text.replace(text[counter], keys_encrypt[text[counter]])
            counter = counter + 1
    if mode[1] == '2':
        counter = 0
        while counter < len(text):
            text = text.replace(text[counter], keys_decrypt[text[counter]])
            counter = counter + 1
else: 
    print("Erro: nenhum modo disponivel selecionado")  



print("OUTPUT: "+text)


