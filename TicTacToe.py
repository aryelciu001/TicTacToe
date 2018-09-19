import random
import string

def print_board(mylist):
    board = '''
        |     |
      {} |  {}  | {}
        |     |
    ---------------    
        |     |
      {} |  {}  | {}
        |     |
    ---------------
        |     |
      {} |  {}  | {}
        |     |
     
    '''.format(mylist[7],mylist[8],mylist[9],mylist[4],mylist[5],mylist[6],mylist[1],mylist[2],mylist[3])
    print(board)
    
def undi_giliran():
    import random
    from random import randint
    player=['X','O']
    one=player.pop(randint(0,1))
    two=player.pop()
    return one,two

    
def input_move(mylist,numofmove):
    if numofmove%2==0:
        print(f'{first} turn now')
    else:
        print(f'{second} turn now')
    print('Insert a number here')
    movestring=input()
    while not spot_available(mylist,movestring):
        print('Please insert a valid number(1-9)')
        movestring=input()
    move=int(movestring)
    return move

def spot_available(mylist,move):
    if str(move) not in string.digits:
        return False
    elif mylist[int(move)] != ' ':
        return False
    else : 
        return True
    
def make_move(first,second,mylist,move,numofmove):
    if numofmove%2 == 0:
        mylist[move]=first
    else:
        mylist[move]=second
    
    return mylist
    
    
def win(mylist):
    if mylist[7]==mylist[8]==mylist[9]=='X' or mylist[7]==mylist[8]==mylist[9]=='O':
        print(f'{mylist[7]} wins!')
        return True
    elif mylist[4]==mylist[5]==mylist[6]=='x' or mylist[4]==mylist[5]==mylist[6]=='O':
        print(f'{mylist[4]} wins!')
        return True
    elif mylist[1]==mylist[2]==mylist[3]=='X' or mylist[1]==mylist[2]==mylist[3]=='O':
        print(f'{mylist[1]} wins!')
        return True
    elif mylist[1]==mylist[4]==mylist[7]=='X' or mylist[1]==mylist[4]==mylist[7]=='O':
        print(f'{mylist[7]} wins!')
        return True
    elif mylist[2]==mylist[5]==mylist[8]=='X' or mylist[2]==mylist[5]==mylist[8]=='O':
        print(f'{mylist[8]} wins!')
        return True
    elif mylist[3]==mylist[6]==mylist[9]=='X' or mylist[3]==mylist[6]==mylist[9]=='O':
        print(f'{mylist[6]} wins!')
        return True
    elif mylist[3]==mylist[5]==mylist[7]=='X' or mylist[3]==mylist[5]==mylist[7]=='O':
        print(f'{mylist[7]} wins!')
        return True
    elif mylist[1]==mylist[5]==mylist[9]=='X' or mylist[1]==mylist[5]==mylist[9]=='O':
        print(f'{mylist[1]} wins!')
        return True
    else:
        return False
        
def playagain():
    print('Play again?')
    ans=input()
    return ans.lower().startswith('y')
    
while True : 
    print('''
WELCOME
    To
    TICTACTOE
    ''')
    undi=undi_giliran()
    first=undi[0]
    second=undi[1]
    print(f'The first person to go is {first}')
    print(f'The second is {second}')
    mylist=[0]+[' ']*9
    numofmove=0
    while True : 
        move=input_move(mylist,numofmove)
        make_move(first,second,mylist,move,numofmove)
        numofmove+=1
        print_board(mylist)
        if win(mylist):
            break
        elif numofmove==9:
            print('TIE')
            break
        elif not win(mylist):
            continue
        
    if not playagain():
        break
