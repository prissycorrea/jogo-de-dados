import random

print(". . . . . . . . . . . . . . . . . . . . . .")
print(". . .   Bem vindo ao jogo dos dados  . . .")
print(". . . . . . . . . . . . . . . . . . . . . .")

iniciar_jogo = input("Deseja lançar o dado? S/N ")

while iniciar_jogo == "Sim" or iniciar_jogo == "SIM" or iniciar_jogo == "sim" or iniciar_jogo == "S" or iniciar_jogo == "s":
        dado = random.randrange(1, 7)
        print(". . . dados rolando . . .")
        print("| ", dado, " |")
        iniciar_jogo = input("Deseja jogar novamente?")
else:
    print(". . . . . . . . . . . . . . . . . . . . . .")
    print(". . . . . . .  Fim de jogo  . . . . . . . .")
    print(". . . . . . . . . . . . . . . . . . . . . .")
