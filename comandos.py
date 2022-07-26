import os
os.listdir("D:/") # lista todos os arquivos existentes no diretório

x = open("D:/teste.txt")
print(x.read) # mostra os detalhes técnicos do arquivo

linhas = x.readlines() # Lê todos as linhas existentes no arquivo
print(linhas)

for i in linhas:
    print(i)
 
z = open("D:/teste3.txt", "w") # cria um novo arquivo     
os.listdir("D:/")

    
