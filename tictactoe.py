def ticTacToe():
  from IPython.display import clear_output
  sair = ''
  vez = 'O'
  placar = {
            'X':0,
            'O':0
              }
  
  tabuleiro = {
      1:'-',
      2:'-',
      3:'-',
      4:'-',
      5:'-',
      6:'-',
      7:'-',
      8:'-',
      9:'-'
  }

  def printBoard(tabuleiro):
    print(tabuleiro[1] + '|' + tabuleiro[2] + '|' + tabuleiro[3] + '\t| 1'+ '|' + '2' + '|' + '3')
    print('-+-+-'+'\t| -+-+-')
    print(tabuleiro[4] + '|' + tabuleiro[5] + '|' + tabuleiro[6] + '\t| 4' + '|' + '5' + '|' + '6')
    print('-+-+-'+ '\t| -+-+-')
    print(tabuleiro[7] + '|' + tabuleiro[8] + '|' + tabuleiro[9] + '\t| 7' + '|' + '8' + '|' + '9')

  def move(vez):
    player = '' 
    if vez == 'O':
      vez = 'X'
      player = 'Jogador 1'
      return [vez, player]
    elif vez == 'X':
      vez = 'O'
      player = 'Jogador 2'
      return [vez, player]
    else:
      print('Opção não encontrada')
  
  def replay(sair,vez,tabuleiro):
    if sair == 'sim':
      print(f'Placar final: \n{placar}')
      return [sair, vez]
    else:
      for posicao in tabuleiro:
        tabuleiro[posicao] = '-'
      return [sair,vez]

  def checkWinner(tabuleiro,vez,player):
    for i in tabuleiro:
      if (tabuleiro[1] == vez and tabuleiro[2] == vez and tabuleiro[3] == vez) or (tabuleiro[4] == vez and tabuleiro[5] == vez and tabuleiro[6] == vez) or (tabuleiro[7] == vez and tabuleiro[8] == vez and tabuleiro[9] == vez):
        print(f'================================================')
        placar[vez] = placar[vez]+1
        print(f'O {player} VENCEU!')
        print(f'================================================')
        sair = input('Deseja Sair? [sim] | [não]: ')
        sair, vez = replay(sair,vez,tabuleiro)
        return sair
      else:
        print('Deu velha')
    sair = ''
    return sair


  while sair != 'sim':    
    clear_output()
    printBoard(tabuleiro)
    vez, player = move(vez)

    jogada = int(input(f'\n\n {player}: Onde você deseja jogar: '))
    tabuleiro[jogada] = vez
    sair = checkWinner(tabuleiro, vez, player)

    
ticTacToe()