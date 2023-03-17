import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_images = ["pedra", "papel", "tesoura"]

escolha_do_usuario = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
print(game_images[escolha_do_usuario])

escolha_do_computador = random.randint(0, 2)
print("O computador escolheu:")
print(game_images[escolha_do_computador])

if escolha_do_usuario >= 3 or escolha_do_usuario < 0:
    print("Você digitou um número inválido, você perdeu!")

elif escolha_do_usuario == 0 and escolha_do_computador == 2:
    print("Você ganhou!")
elif escolha_do_computador == 0 and escolha_do_usuario == 2:
    print("Você perdeu")
elif escolha_do_computador > escolha_do_usuario:
    print("Você perdeu")
elif escolha_do_usuario > escolha_do_computador:
    print("Você ganhou!")
elif escolha_do_computador == escolha_do_usuario:
    print("Empate")

