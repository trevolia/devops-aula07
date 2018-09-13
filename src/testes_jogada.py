import jogovelha
import sys

erroInicializar = False

jogovelha.jogar()
jogada = jogovelha.jogar()
num_coluna=input(int("Digite o número da coluna"))
num_linha=input(int("Digite o número da linha"))


if num_coluna in jogada and num_linha in jogada:
    erroJogada = True
else:
    jogada.append(num_coluna)
    jogada.append(num_linha)

if erroInicializar:
      print('Erro!')
      sys.exit(1)
else:
      sys.exit(0)
