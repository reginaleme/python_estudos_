# ------------------- ARQUIVOS ---------------------------

# lista todos os arquivos existentes no diretório
import os
os.listdir("D:/") 


# mostra os detalhes técnicos do arquivo
x = open("D:/teste.txt")
print(x.read) 


# Lê todos as linhas existentes no arquivo
linhas = x.readlines() 
print(linhas)

for i in linhas:
    print(i)
    
 
# cria um novo arquivo     
z = open("D:/teste5.txt", "w")     # o "w" sempre irá criar um novo arquivo
os.listdir("D:/")                  # se existir um arquivo com o mesmo nome,
                                   # sobrepoe


# insere dados no arquivo
z.write("inserindo dados no arquivo \n")
z.close()
v = z.readlines()


# o "a" irá abrir o arquivo já existente
z = open("D:/teste5.txt", "a")     
z.write("inserindo dados no arquivo 5 \n")
z.close()




# ------------------- LISTAS --------------------

# criando uma lista e mostrando uma determinada posição
minha_lista = [1, "regina", 9.99]
print(minha_lista[2])

for i in minha_lista:
    print(i)
    
    
# verificando o tamanho da lista  
tamanho = len(minha_lista)
print(tamanho)


# incluindo itens na minha lista
minha_lista.append("novo item")
print(minha_lista)


# criando uma lista vazia
minha_lista_2 = []
print(minha_lista_2)


# ordenando a lista em ordem crescente
minha_lista_3 = [5,9,1,6,8]
print(minha_lista_3)

minha_lista_3.sort() # ele atribui a nova ordenação direto na variável
print(minha_lista_3)


# o sosrted ordena a lista mas precisa atribuir o resultado a uma variavel
minha_lista_4 = sorted(minha_lista_3)
print(minha_lista_4)



# ordenando a lista em ordem crescente
minha_lista_6 = ["regina", "benedito", "ana"]
print(minha_lista_6)

minha_lista_6.sort() # ele atribui a nova ordenação direto na variável
print(minha_lista_6)


# para reverter a ordenação
minha_lista_6.sort(reverse=True) # ele atribui a nova ordenação direto na variável
print(minha_lista_6)


# para trocar as ordens dos dados
minha_lista_6.reverse() # ele atribui a nova ordenação direto na variável
print(minha_lista_6)




# ------------------- DICIONÁRIO - ARRAYS --------------------

array = {"a": "ameixa", "b": "boca", "c":"cachorro"}
print(array["a"]) # vai imprimir os dados da chave "a"
print(array) # vai imprimir os dados do array todo

# imprime as chaves e seus valores
for i in array:
    print(i + "-" + array[i])


# converte o array em uma tupla e exibe chave + seus valores
for i in array.items():
    print(i)
    
    
# exibe somente os seus valores
for i in array.values():
    print(i)
    
    
# exibe somente as chaves
for i in array.keys():
    print(i)
    
    
# ------------------- RETORNAR NUMEROS ALEATÓRIOS --------------------
import random

random.seed(5) # comando para fixar um número
numero = random.randint(0,10) # comando para escolher aleatório de 0 a 10
print(numero)


lista = [5,49,62]
numero = random.choice(lista) # comando para escolher aleatório o conteudo de lista
print(numero)



# ------------------- TRATAMENTO DE EXCEÇÕES --------------------
a = 2
b = 0

try:
    print(a / b)
except:
    print("Não é permitido divisão por zero")
    
    
    

# ------------------- LIST COMPREHENSION --------------------
x = [1,2,3,4,5]
y = []

for i in x:
    y.append(i**2)
    
print(x)
print(y)


# usando a list comprehension
x = [1,2,3,4,5]
#y = [valor_a_adicionar laco condicao]
y = [i**2 for i in x]

print(x)
print(y)


# imprimindo somente número impar (usando a parte da condicao agora)
x = [1,2,3,4,5]
z = [i for i in x if i%2==1]

print(z)



# ------------------- FUNCAO ENUMERATE --------------------
lista = ["abacaxi", "regina", "uva"]

for i, nome in enumerate(lista):
    print(i, nome)
    
    
    
# ------------------- FUNCAO MAP --------------------
# pega uma função e aplica para todos os itens da lista
#map(função, lista)

def dobro(x):
    return x*2

valor = [1,2,3,4,5]
valor_dobrado = map(dobro, valor)

for i in valor_dobrado:
    print(i)
    

# convertendo para uma lista    
valor_dobrado = list(valor_dobrado)    
print(valor_dobrado)




# ------------------- FUNCAO REDUCE --------------------
# recebe uma lista e retorna somente um valor dessa lista

from functools import reduce

def soma(x,y):
    return x+y

lista = [1,2,5,6,8]

#soma = reduce(funcao, lista)
soma = reduce(soma, lista)
print(soma)



# ------------------- FUNCAO ZIP --------------------
# concatena 2 ou mais listas

lista1 = [1,2,3,4,5]
lista2 = ["a", "b", "c", "d", "e"]
lista3 = ["abacate", "bola", "cachorro", "dado", "elefante"]

for numero, letra, descricao in zip(lista1, lista2, lista3):
    print(numero, letra, descricao)
    
    
    
# ------------------- FILTER --------------------
# filtra os valores retornados na função dentro da lista

lista = [1,5,6,2,7]

def par(x):
    if x%2==0:
        return x

#lista2 = filter(funcao, lista)
lista2 = filter(par, lista)

for x in lista2:
  print(x)

