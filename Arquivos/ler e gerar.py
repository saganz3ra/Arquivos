import random

nomes = ["Rafael", "Allan", "Eduardo", "Victor", "Pedro", "Guilherme", "Iuri", "Andrey", "Carlos", "Jacinto",
         "Vinicius", "Luiz", "Richard", "Gustavo", "Alberto", "Galvão", "Casimiro", "Daniel", "Edgar"]
sobrenomes = ["Sagan", "Bida", "Cenni", "Augusto", "Goes", "Chimia", "Souza", "Silva", "Claro", "Pinto",
              "Ferraz", "Manco", "Oliveira", "Luiz", "David", "Oliveira", "Jon", "Carpenter", "Cameron"]

def gerarNomes():
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    return f"{nome} {sobrenome}"

def gerarIdade():
    return random.randint(18, 99)

N = int(input("Digite o número de nomes a serem gerados: "))

with open("nomes_e_idades.txt", "w") as arquivo:
    for _ in range(N):
        nomeCompleto = gerarNomes()
        idade = gerarIdade()
        arquivo.write(f"{nomeCompleto}, {idade} anos\n")

print(f"{N} nomes e idades aleatórios foram gerados e salvos no arquivo 'nomes_e_idades.txt'.")