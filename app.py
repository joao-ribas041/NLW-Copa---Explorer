import os

source = r"C:\Users\Joao-Ribas\Documents\Dev\Projetos\NLW Copa - Explorer\assets\paises1"
dest = r"C:\Users\Joao-Ribas\Documents\Dev\Projetos\NLW Copa - Explorer\assets\paises2"
arquivos = os.listdir(source)
cont = 0

for arquivo in arquivos:
    old = arquivo
    new = arquivo.replace("=", "-")
    os.rename(source + '/' + old, dest + '/' + new)

print("Sucess")


""" for arquivo in arquivos:
    print(arquivo)
    cont += 1
print(cont) """
    