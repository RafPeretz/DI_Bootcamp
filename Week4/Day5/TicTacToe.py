# tic tac toe
def play():
    name_player1 = input("the name of the first player")
    name_player2 = input("the name of the second player")
    winner = "false"
    tour = 1
    board = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
    while(winner == "false" and tour != 10):
        if(tour % 2 != 0):
            print(f"{name_player1} it s your time to play")
            x = int(input("which row"))
            y = int(input("which colun"))
            moove(x,y,board,tour%2)
        else:
            print(f"{name_player2} it s your time to play")
            x = int(input("which row"))
            y = int(input("which colun"))
            moove(x, y, board,tour%2)
        display_board(board)
        winner = check_borad(board)
        if(winner == "true"):
            if(tour % 2 != 0):
                print(f"congradulation {name_player1} you win")
            else:
                print(f"congradulation {name_player2} you win")
        tour +=1
    if(tour == 10 ):
        print("no one win the game")




def moove(row,colun,arr,plr):

    while arr[row][colun] != " ":
        print("cheat are not alowed here please replay corectely")
        display_board(arr)
        row = int(input("give me a new num for rows"))
        colun = int(input("give me a new num for colun"))
    if plr == 1 :
        arr[row][colun] = "X"
    else:
        arr[row][colun] = "O"

def display_board(arr):
    print("***********")
    for i in range(0,3):
        print("* "+arr[i][0]+"| "+arr[i][1]+" |"+arr[i][2]+" *")
        if i != 2 :
            print("*--|---|--*")

    print("***********")

def check_borad(arr):
    boole = "false"
    vide = ""
    for i in range(0,3):
        if arr[i][0] == arr[i][1] and arr[i][2] == arr[i][1]:
            if arr[i][0] ==" ":
                continue
            else:
                boole = "true"
        elif arr[0][i] == arr[1][i] and arr[2][i] == arr[1][i]:
            if arr[0][i] == " ":
                continue
            else:
                boole = "true"
    if(arr[0][0] == arr[1][1] and arr[2][2] == arr[1][1]):
        if arr[1][1] == " ":
            vide+=" "
        else:
            boole = "true"
    elif(arr[0][2] == arr[1][1] and arr[2][0] == arr[1][1]):
        if arr[1][1] == " ":
            vide += " "
        else:
            boole = "true"
    return boole
play()