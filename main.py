#Definir o jogador
#Criar o mapa
#Fazer o input do jogador
#Realizar a jogada
#Proximo jogador
#Ganhou o Jogo da velha? Finalizar

def definir_player():
    
    player1 = 'wrong'
    while player1 not in ['X','O']:
        player1 = input('Você quer seu o jogador X ou O: ')
    print(f"Você definiu o jogador {player1}")
    player2 = ''
    if player1 == 'X':
        player2 = 'O'
    elif player1 == 'O':
        player2 = 'X'
    return player1,player2

def jogoDaVelhaVisual(map):

    print(map[7:10])
    print ("----------------")
    print(map[4:7])
    print ("----------------")
    print(map[1:4])


def jogada():
    
    jogada = ''
    jogadasValidas = range(1,10)
    print(jogadasValidas)
    while not jogada in jogadasValidas:
        
        jogadaInput = input("Digite a jogada que você quer realizar (1-9): ")

        if jogadaInput.isnumeric():
            jogadaInput =int(jogadaInput)
            if jogadaInput < 9:
                jogada = jogadaInput
            else:
                print("A sua jogada deve ser entre 1-9")
        else:
            print("A sua jogada deve ser um número entre 1-9")
    return jogadaInput

def jogo(map,jogada,player1,player2,vezDoJogador):
    verificarJogada = True
    if map[jogada] == 'X' or map[jogada] == 'O':
        while verificarJogada:
            jogada = input("Essa jogada já foi realizada, digite um novo número (1-9): ")
            if jogada.isnumeric():
                jogada = int(jogada)
                if jogada < 10 and not map[jogada] == 'X'  and not map[jogada] == 'O':
                    verificarJogada = False
    if vezDoJogador == 0:
        map[jogada] = player1
        vezDoJogador =+ 1
        print(f'Vez do jogador {player2}')

    elif vezDoJogador == 1:
        map[jogada] = player2
        vezDoJogador = vezDoJogador - 1
        print(f'Vez do jogador {player1}')
    else:
        print('nenhum')
    return map,vezDoJogador
def verificarVitoria(map,player1,player2):


    #Verificar as linhas horizontais

    if map[1] == player1 and map[2] == player1 and map[3] == player1 or map[1] == player2 and map[2] == player2 and map[3] == player2:
        jogoDaVelhaVisual(map)
        print("Venceu")
        return False
    elif map[4] == player1 and map[5] == player1 and map[6] == player1 or map[4] == player2 and map[5] == player2 and map[6] == player2:
        jogoDaVelhaVisual(map)
        print("Venceu")
        return False
    elif map[7] == player1 and map[8] == player1 and map[9] == player1 or map[7] == player2 and map[8] == player2 and map[9] == player2:
        jogoDaVelhaVisual(map)
        print("Venceu")
        return False
    elif map[1] == player1 and map[4] == player1 and map[7] == player1 or map[1] == player2 and map[4] == player2 and map[7] == player2:
        jogoDaVelhaVisual(map)
        print("Venceu")
        return False
    elif map[2] == player1 and map[5] == player1 and map[8] == player1 or map[2] == player2 and map[5] == player2 and map[8] == player2:
        jogoDaVelhaVisual(map)
        print("Venceu")
        return False
    elif map[3] == player1 and map[6] == player1 and map[9] == player1 or map[3] == player2 and map[6] == player2 and map[9] == player2:
        jogoDaVelhaVisual(map)
        print("Venceu")
        return False
    elif map[1] == player1 and map[5] == player1 and map[9] == player1 or map[1] == player2 and map[5] == player2 and map[9] == player2:
        jogoDaVelhaVisual(map)
        print("Venceu")
        return False
    elif map[3] == player1 and map[5] == player1 and map[7] == player1 or map[3] == player2 and map[5] == player2 and map[7] == player2:
        jogoDaVelhaVisual(map)
        print("Venceu")
        return False
    elif not ' ' in map:
        print("Empate")
        return False
    else:
        return True


map = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
vezDoJogador = 0
player1,player2 = definir_player()
Jogando = True
while Jogando:
    jogoDaVelhaVisual(map)
    jogadar = jogada()
    map,vezDoJogador = jogo(map,jogadar,player1,player2,vezDoJogador)
    Jogando = verificarVitoria(map,player1,player2)


