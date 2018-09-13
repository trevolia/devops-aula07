# Arquitetura
## Inicialização do tabuleiro
* As funções relacionadas ao gerenciamento das casas do jogo da velha ficarão
no módulo **jogovelha.py**.
* O estado de cada casa do jogo será representada por uma string: "." para casa
vazia; "X" para casa ocupada pelo 1o jogador; "O" para casa ocupada pelo 2o
jogador
* A função inicializar() retornará uma lista 3x3, onde cada posição conterá uma
string para indicar o estado de uma casa do jogo. A função retornará todas as
casas inicialmente vazias.
* A função jogar(jogador, linha, coluna) irá posicionar o **jogador** ('X' ou
'O') na posição definida por **linha** e **coluna**.

*  NÃO SERÁ POSSIVEL QUE O 1° JOGADOR CONSIGA PREENCHER UM LUGAR JA PREENCHIDO.
UMA FUNÇÃO DE VERIFICAÇÃO DE POSIÇÕES RETORNARÁ TODAS AS POSIÇÕES. CASO A POSIÇÃO JÁ ESTEJA OCUPADA,
A FUNÇÃO DEVERÁ RETORNAR TRUE. UMA OUTRA FUNÇÃO DE VALIDAÇÃO SERÁ RESPONSÁVEL EM 
ENVIAR UMA MENSAGEM DO TIPO "NÃO É POSSÍVEL EFETUAR ESTA JOGADA" CHAMANDO NOVAMENTE A FUNÇÃO JOGAR(JOGADOR,LINHA,COLUNA).
