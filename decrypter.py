import sys
import os
import pyaes

## abrir o arquivo criptografado
file_name = sys.argv[1]
#file_name = "mensagem-importante.txt.ransomware"

file = open(file_name, "rb") ##rb = read
file_data = file.read()
file.close()

## chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = file_name.replace(".ransomware", "")
new_file = open(f'{new_file}', "wb") #wb = write
new_file.write(decrypt_data)
new_file.close()
