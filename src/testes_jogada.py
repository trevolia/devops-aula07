import tabuleiro
import sys

erroInicializar = False

jogada = tabuleiro.jogar()
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
