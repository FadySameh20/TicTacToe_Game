l = [['-', '|', '-', '|', '-'], ['-', '|', '-', '|', '-'], ['-', '|', '-', '|', '-']]
win = False
row = 0
column = 0
p = 0


def printBoard():
    global l
    for r in l:
        for c in r:
            print(c, end="")
        print()


def newInput(flag):
    global l, p
    if (p == 1):
        if flag == False:
            l[0][0] = "X"
        else:
            l[0][0] = "O"
    elif (p == 2):
        if flag == False:
            l[0][2] = "X"
        else:
            l[0][2] = "O"
    elif (p == 3):
        if flag == False:
            l[0][4] = "X"
        else:
            l[0][4] = "O"
    elif (p == 4):
        if flag == False:
            l[1][0] = "X"
        else:
            l[1][0] = "O"
    elif (p == 5):
        if flag == False:
            l[1][2] = "X"
        else:
            l[1][2] = "O"
    elif (p == 6):
        if flag == False:
            l[1][4] = "X"
        else:
            l[1][4] = "O"
    elif (p == 7):
        if flag == False:
            l[2][0] = "X"
        else:
            l[2][0] = "O"
    elif (p == 8):
        if flag == False:
            l[2][2] = "X"
        else:
            l[2][2] = "O"
    elif (p == 9):
        if flag == False:
            l[2][4] = "X"
        else:
            l[2][4] = "O"


def checkPosition():
    global l, p, row, column
    if p < 1 or p > 9:
        print("Invalid position")
        print()
        return False
    if l[row][column] == "X" or l[row][column] == "O":
        print("Position already occupied")
        print()
        return False
    return True


def setRowColumn():
    global p, row, column
    if p == 1:
        row = 0
        column = 0
    elif p == 2:
        row = 0
        column = 2
    elif p == 3:
        row = 0
        column = 4
    elif p == 4:
        row = 1
        column = 0
    elif p == 5:
        row = 1
        column = 2
    elif p == 6:
        row = 1
        column = 4
    elif p == 7:
        row = 2
        column = 0
    elif p == 8:
        row = 2
        column = 2
    elif p == 9:
        row = 2
        column = 4


def checkWin():
    global l, win
    if ((l[0][0] == l[0][2] == l[0][4]) and (l[0][0] != '-')) or (
            (l[0][0] == l[1][0] == l[2][0]) and (l[0][0] != '-')) or (
            (l[0][0] == l[1][2] == l[2][4]) and (l[0][0] != '-')) or (
            (l[0][4] == l[1][4] == l[2][4]) and (l[0][4] != '-')) or (
            (l[0][4] == l[1][2] == l[2][0]) and (l[0][4] != '-')) or (
            (l[2][0] == l[2][2] == l[2][4]) and (l[2][0] != '-')) or (
            (l[0][2] == l[1][2] == l[2][2]) and (l[0][2] != '-')) or (
            (l[1][0] == l[1][2] == l[1][4]) and (l[1][0] != '-')):
        win = True


def checkFullBoard():
    global l
    count = 0
    for r in l:
        for c in r:
            if c == '-':
                count = count + 1
    if count == 0:
        return True
    return False


def validateInput(player):
    global p
    while True:
        try:
            print(player)
            print("Enter position:", end=" ")
            p = int(input())
            break
        except:
            print("Invalid input")
            print()
    setRowColumn()


def switchTurns(flag):
    global win
    if flag == False:
        player = "Player 1"
    else:
        player = "Player 2"
    validateInput(player)
    while checkPosition() == False:
        validateInput(player)
    newInput(flag)
    print()
    printBoard()
    print()
    checkWin()
    if win == True:
        if flag == False:
            print(player + " won !!")
            return False
        else:
            print(player + " won !!")
    return True


def playGame():
    global win
    print()
    printBoard()
    print()
    while win == False:
        if switchTurns(False) == False:
            break
        if checkFullBoard() == True:
            print("Tie !")
            break
        switchTurns(True)


playGame()