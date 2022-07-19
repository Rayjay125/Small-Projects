import copy
import os

def liveChar():
    return 0.01
def deadChar():
    return 1111

def decision(liveN, state):
    if state == liveChar():
        if liveN < 2: return deadChar()
        if liveN == 2: return liveChar()
        if liveN == 3: return liveChar()
        if liveN > 3: return deadChar()
    if state == deadChar():
        if liveN < 3: return deadChar()
        if liveN == 3: return liveChar()
        if liveN > 3: return deadChar()
        

###################
###################

def checkOnlyMid(i,j):
    liveN = 0
    if j == 0: 
        if board[i][j+1] == liveChar(): liveN += 1
    elif j == (len(board[0])-1): 
        if board[i][j-1] == liveChar(): liveN += 1
    else:
        if board[i][j+1] == liveChar(): liveN += 1
        if board[i][j-1] == liveChar(): liveN += 1
    nextstep[i][j] = decision(liveN, board[i][j])
    
###################

def checkOnlyVert(i,j):
    liveN = 0
    if i == 0: 
        if board[i+1][j] == liveChar(): liveN += 1
    elif i == (len(board)-1): 
        if board[i-1][j] == liveChar(): liveN += 1
    else:
        if board[i+1][j] == liveChar(): liveN += 1
        if board[i-1][j] == liveChar(): liveN += 1
    nextstep[i][j] = decision(liveN, board[i][j])

###################
###################

def checkTopLeft(i,j):
    liveN = 0
    if board[i+1][j] == liveChar(): liveN += 1
    if board[i+1][j+1] == liveChar(): liveN += 1
    if board[i][j+1] == liveChar(): liveN += 1
    nextstep[i][j] = decision(liveN, board[i][j])
    
def checkTopMid(i,j):
    liveN = 0
    if board[i+1][j] == liveChar(): liveN += 1
    if board[i+1][j+1] == liveChar(): liveN += 1
    if board[i][j+1] == liveChar(): liveN += 1
    if board[i+1][j-1] == liveChar(): liveN += 1
    if board[i][j-1] == liveChar(): liveN += 1
    nextstep[i][j] = decision(liveN, board[i][j])
    
def checkTopRight(i,j):
    liveN = 0
    if board[i+1][j] == liveChar(): liveN += 1
    if board[i+1][j-1] == liveChar(): liveN += 1
    if board[i][j-1] == liveChar(): liveN += 1
    nextstep[i][j] = decision(liveN, board[i][j])

#############

def checkMidLeft(i,j):
    liveN = 0
    if board[i+1][j] == liveChar(): liveN += 1
    if board[i+1][j+1] == liveChar(): liveN += 1   
    if board[i][j+1] == liveChar(): liveN += 1  
    if board[i-1][j] == liveChar(): liveN += 1 
    if board[i-1][j+1] == liveChar(): liveN += 1
    nextstep[i][j] = decision(liveN, board[i][j])
    
def checkMidMid(i,j):
    liveN = 0
    #positive and neutral j
    if board[i+1][j] == liveChar(): liveN += 1
    if board[i+1][j+1] == liveChar(): liveN += 1   
    if board[i][j+1] == liveChar(): liveN += 1  
    if board[i-1][j] == liveChar(): liveN += 1 
    if board[i-1][j+1] == liveChar(): liveN += 1
    #negative j
    if board[i+1][j-1] == liveChar(): liveN += 1
    if board[i][j-1] == liveChar(): liveN += 1
    if board[i-1][j-1] ==liveChar(): liveN += 1
    nextstep[i][j] = decision(liveN, board[i][j])
    
def checkMidRight(i,j):
    liveN = 0
    if board[i+1][j] == liveChar(): liveN += 1
    if board[i+1][j-1] == liveChar(): liveN += 1
    if board[i][j-1] == liveChar(): liveN += 1
    if board[i-1][j-1] == liveChar(): liveN += 1
    if board[i-1][j] == liveChar(): liveN += 1
    nextstep[i][j] = decision(liveN, board[i][j])

###################

def checkBottomLeft(i,j):
    liveN = 0
    if board[i][j+1] == liveChar(): liveN += 1  
    if board[i-1][j] == liveChar(): liveN += 1 
    if board[i-1][j+1] == liveChar(): liveN += 1
    nextstep[i][j] = decision(liveN, board[i][j])
    
def checkBottomMid(i,j):
    liveN = 0
    #positive and neutral j
    if board[i][j+1] == liveChar(): liveN += 1  
    if board[i-1][j] == liveChar(): liveN += 1 
    if board[i-1][j+1] == liveChar(): liveN += 1
    #negative j
    if board[i][j-1] == liveChar(): liveN += 1
    if board[i-1][j-1] ==liveChar(): liveN += 1
    nextstep[i][j] = decision(liveN, board[i][j])
    
def checkBottomRight(i,j):
    liveN = 0
    if board[i][j-1] == liveChar(): liveN += 1
    if board[i-1][j-1] == liveChar(): liveN += 1
    if board[i-1][j] == liveChar(): liveN += 1
    nextstep[i][j] = decision(liveN, board[i][j])

#############################################
    
def answerValidation(possibleAnswers):
    ans = int(input("Type a relevant numberic answer to continue: "))
    while ans not in possibleAnswers:
        print("\nInvalid answer. Please choose a valid answer from the options available: \n")
        ans = int(input("Would you like to enter a new starting state [1], or view an example [2]? : "))
    return ans
    
def startingPrompt():
    possibleAnswers = [1,2]
    print("Would you like to enter a new starting state [1], or view an example [2]? \n")
    ans = answerValidation(possibleAnswers)
        
    if ans == 1: 
        live = input("\nWhat is your live-state character/number in your input? \n")
        dead = input("What is your dead-state character/number in your input? \n")
        print("Enter the starting state using a space to print the next row e.g.")
        print(dead,live,dead," ",dead,dead,live," ",live,live,live," ",dead,dead,dead,"\nor type [example] to use the above example start state \n")
        answer = input()
        liveDisplay = input("What character/number would you like to use to display live cells?: ")
        deadDisplay = input("\nWhat character/number would you like to use to display dead cells?: ")
        print("\n")
    elif ans == 2:
        answer = "11111111111 11111111111 11111111111 11111111111 11111111111 11118881111 11118181111 11118881111 11118881111 11118881111 11118881111 11118181111 11118881111 11111111111 11111111111 11111111111 11111111111 11111111111"
        live = "8"
        dead = "1"
        liveDisplay = "O"
        deadDisplay = " "
    
    board = []
    if answer == "example":
        board = [[deadChar(),liveChar(),deadChar()],[deadChar(),deadChar(),liveChar()],[liveChar(),liveChar(),liveChar()],[deadChar(),deadChar(),deadChar()]]
    else:
        board.append([])
        for i in answer:
            if i== " ":
                board.append([])
            else:
                if i == live:
                    print("live")
                    board[-1].append(liveChar())
                else:
                    print("dead")
                    board[-1].append(deadChar())
    
    if ans == 2:
        return [board, liveDisplay, deadDisplay, 0.5]
        
    possibleAnswers = [1,2]
    print("Would you like to change state automatically [1] or toggle changes in state by yourself [2] ?: ")
    nextMethod = answerValidation(possibleAnswers)
    if nextMethod == 1:
        suspend = 0.5
    else:
        suspend = None
                
    return [board, liveDisplay, deadDisplay, suspend]
    
def displayBoard(board, liveDisplay, deadDisplay):
    for i in board:
        row = []
        for j in i:
            if j == liveChar():
                row.append(liveDisplay)
            elif j == deadChar():
                row.append(deadDisplay)
        print(row, "\n")
    print("\n")

####################

import time

initialization = startingPrompt()
board = initialization[0]
liveDisplay = initialization[1]
deadDisplay = initialization[2]
suspend = initialization[3]


cont = "y"
nextstep = copy.deepcopy(board)


os.system("clear")
print("The starting state is: \n")
displayBoard(board, liveDisplay, deadDisplay)
input("Press any key to continue: ")


while cont == "y" or cont == "Y":
    if len(board) == 1 and len(board[0]) == 1: 
        board[0][0] = 0
        pass
    
    if len(board) > 1 and len(board[0]) > 1:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i==0:
                    if j==0: checkTopLeft(i,j)
                    elif j==(len(board[0])-1): checkTopRight(i,j)
                    else:
                        checkTopMid(i,j)

                elif i==(len(board)-1):
                    if j==0: checkBottomLeft(i,j)
                    elif j==(len(board[0])-1): checkBottomRight(i,j)
                    else:
                        checkBottomMid(i,j)

                else:
                    if j==0: checkMidLeft(i,j)
                    elif j==(len(board[0])-1): checkMidRight(i,j)
                    else:
                        checkMidMid(i,j)                  
    elif len(board) == 1 and len(board[0]) > 1:
        for i in range(len(board)):
            for j in range(len(board[0])):
                checkOnlyMid(i,j)  
    else:
        for i in range(len(board)):
            for j in range(len(board[0])):
                checkOnlyVert(i,j)
                
    #editting the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = nextstep[i][j]
    
    os.system("clear")
    if not suspend:
        print("The next state is: \n")
    
    displayBoard(board, liveDisplay, deadDisplay)
    
    if suspend:
        time.sleep(suspend)
    else:
        cont = input("Do you wish to continue? [y/n]")

                






