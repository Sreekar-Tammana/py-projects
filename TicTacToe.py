def draw():
    # this fucntion shows board on output screen
    print(f'\t    {board[1]} |  {board[2]}  |  {board[3]}  ')
    print('\t      |     |       ')
    print('\t--------------------')
    print(f'\t    {board[4]} |  {board[5]}  |  {board[6]}  ')
    print('\t      |     |       ')
    print('\t--------------------')
    print(f'\t    {board[7]} |  {board[8]}  |  {board[9]}  ')
    print('\t      |     |       \n')
    print('\t     PLAYER 1 - X\n\t     PLAYER 2 - O\n')

def checkWin():
    # 1 is for wim game
    # 0 is for game draw
    #-1 is for game is still going on
    if board[1]==board[2] and board[2]==board[3]:
        return 1

    elif board[4]==board[5] and board[5]==board[6]:
        return 1

    elif board[7]==board[8] and board[8]==board[9]:
        return 1

    elif board[1]==board[5] and board[5]==board[9]:
        return 1

    elif board[3]==board[5] and board[5]==board[7]:
        return 1

    elif board[1]==board[4] and board[4]==board[7]:
        return 1

    elif board[2]==board[5] and board[5]==board[8]:
        return 1

    elif board[3]==board[6] and board[6]==board[9]:
        return 1

    elif board[1]!='1' and board[2]!='2' and board[3]!='3' and board[4]!='4' and board[5]!='5' and board[6]!='6' and board[7]!='7' and board[8]!='8' and board[9]!='9':
        return 0

    else:
        return -1

if __name__ == "__main__":
    print('\t********WELCOME TO TIC TAC TOE PLAY BOARD********\n')
    board = ['0','1','2','3','4','5','6','7','8','9']
    player = 1 #By default player value will be 1 as the loop iterates player value will be increased
    draw()

    while True:

        if player%2==1:
            player = 1
            mark = 'X'
            print('PLAYER 1 turn**')
            choice = int(input('Choose a number : '))
        else:
            player = 2
            mark = 'O'
            print('PLAYER 2 turn**')
            choice = int(input('Choose a number  : '))

        if choice==1 and board[1]=='1':
            board[1] = mark

        elif choice==2 and board[2]=='2':
            board[2] = mark

        elif choice==3 and board[3]=='3':
            board[3] = mark
        
        elif choice==4 and board[4]=='4':
            board[4] = mark

        elif choice==5 and board[5]=='5':
            board[5] = mark

        elif choice==6 and board[6]=='6':
            board[6] = mark

        elif choice==7 and board[7]=='7':
            board[7] = mark

        elif choice==8 and board[8]=='8':
            board[8] = mark

        elif choice==9 and board[9]=='9':
            board[9] = mark

        else:
            print('INVALID...')
            player-=1

        draw()

        i=checkWin() #for every iteration this checks whether the game is over or still playing

        player+=1 #this increments the player value

        if i==1:
            print(f'Player {player-1} wins')
            break
        elif i==-1:
            continue
        else:
            print('Game Draw')