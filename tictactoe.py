import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='x'
p2s='o'


def place(symbol):
    print(numpy.matrix(board))
    while True:
        row=int(input('Enter row 1/2/3: '))
        col=int(input('Enter col 1/2/3: '))
        
        if(row>0 and col>0 and row<4 and col<4 and board[row-1][col-1]=='-'):
            break
        else:
            print('Enter a valid input')
            
    board[row-1][col-1]=symbol
        
        
def check_row(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
                
        if count==3:
            print(symbol,'won')
            return True
    return False

def check_diagonal(symbol):
    if board[0][0]==symbol and board[1][1]==symbol and board[2][2]==symbol:
        print(symbol,'won')
        return True
    
    elif(board[0][2]==symbol and board[1][1]==symbol and board[2][0]==symbol):
        print(symbol,'won')
        return True
    else:
        return False
        
    
    
    
    
    
    
    
def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
                
        if count==3:
            print(symbol,'won')
            return True
    return False
            
            
        
def won(symbol):
    return check_row(symbol) or check_col(symbol) or check_diagonal(symbol)


def play():
    for turn in range (9):
        if turn%2==0:
            print('x turn')
            place(p1s)
            if won(p1s):
                break
            
        else:
            print('o turn')
            place(p2s)
            if won(p2s):
                break
            
            
    if not(won(p1s)) and not(won(p2s)):
        print('draw')
        
        
play()
        