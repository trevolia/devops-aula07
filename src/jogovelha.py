TAB = []

def inicializar() :
  TAB.append(['.','.','.'])
  TAB.append(['.','X','.'])
  TAB.append(['.','.','.'])

def jogar(jogador, linha, coluna):
  if jogador !='X' and jogador != 'O':
    raise RuntimeError('Jogador inválido!')
  valores = list(range(0,3))
  if linha not in valores:
    raise RuntimeError('Linha inválida!')
  if coluna not in valores:
    raise RuntimeError('Coluna inválida!')
  if TAB[linha][coluna] == jogador:
    raise RuntimeError('Posição já tomada!')
  TAB[linha][coluna] = jogador

def tabuleiro():
  return TAB

def main():
  inicializar()
  jogar('X', 1, 1)
  print(tabuleiro())
  
if __name__ == "__main__":
  main()
