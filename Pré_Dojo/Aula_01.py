from pprint import pprint # importacao para imprimir dicionarios de forma melhor ( Recurso comestico apenas)


valor = 42
valor2 = "hype ta em hype" # Nao precisamos declarar o tipo
valor3 = [0,1,2,3,4] # python por ser dinamico nao tem arrays, apenas listas

print(valor, "-->", type(valor)) # type verifica o tipo da variavel
print(valor2, "-->", type(valor2))
print(valor3,"-->", type(valor3))

noNumber = (int)("10") #typecast
number = 10
print(noNumber + number)

string, numero, numero_real = "Oii", 5, 3.5 # podemos delcarar varias variaveis de tipos diferentes na mesma linha

#Tupla: lista de elementos que nao pode ser alterada
tupla1 = ["pão", 34.2]

intervalo = range(10) # intervalo de valores
Nulo = None # valor q atribuir nulo a uma variavel
print(3**4) # ** sinaliza a potenciação
str1 = "meu nombre"
str2 = "carlo"
print((str1*3 ) + str2) 
#input1 = input("digite por favor: ")

verdade = False #booleanos declarados com letra maiuscula, se nao sao tratados como uma variavel

if verdade == True:
    print("é verdade")
else: # temos tbm elif, que basicamente é um else if
    print("é mentira")

    #Lista: tamanho variavel e podemso armazenar qualquer valor
lista = list() # ou assim lista = []

lista.append("Python")
lista.append(3)
lista.append(["Um","exemplo", "de", "tupla"])
lista.append(4.32)
print(lista[0], lista[1], lista[2])
print(lista[-1], lista[-2], lista[-3]) # -1: imprime o ultimo, -2: imprime o penultimo, etc
#slices
print("1 ->", lista[1:3]) # do segundo ao terceiro elemento ( o 3 fora do slice)
print("2 ->", lista[:2]) # tpdps ps eçe,emtps ate a segndaposicao
print("3 ->", lista[1:]) # todos elementos a partir da segunda posicao
print("4 - >", lista[-1]) # excluidno o primeuiuro elemento?
print("5 ->", lista[:]) # imprimindo tudo

lista.reverse # inverte a lista
lista.reverse # inverte a lista

tuplaTeste =("tralalero", 32, True)
print(tuplaTeste[0], tuplaTeste[-1]) #print de dupla funciona q nem lista

# dicionarios ao lsitas com indices de string ao inves de inteiros

#dicio.update: adiciona mais campos no dicionario

dicio = {
    "tamanho": 20,
    "mensagem": "pina colada",
    "editora": "vaivo"
}

input1 = int(input("digite valor 1: "))
input2 = int(input("digite valor 2: "))
print(input1 + input2)