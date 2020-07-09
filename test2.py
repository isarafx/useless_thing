table = ["0", "1", "2",
         "3", "4", "5",
         "6", "7", "8"]
"""
0 / 1 / 2
----------
3 / 4 / 5
----------
6 / 7 / 8
"""
def displayboard():
    print("\n")
    print(table[0] + " / " + table[1] + " / " + table[2])
    print("----------")
    print(table[3] + " / " + table[4] + " / " + table[5])
    print("----------")
    print(table[6] + " / " + table[7] + " / " + table[8])
def playOX():
    player = 'x'
    win = False
    for x in range(1,10):
        turn = x
        displayboard()

        #check winning condition
        if (table[0] == table[1] == table[2]) or\
            (table[3] == table[4] == table[5]) or\
            (table[6] == table[7] == table[8]) or\
            (table[0] == table[3] == table[6]) or\
            (table[1] == table[4] == table[7]) or\
            (table[2] == table[5] == table[8]) or\
            (table[0] == table[4] == table[8]) or\
            (table[6] == table[4] == table[2]) :
            if player == 'x': # o win
                print("Congratulation, O won!")
            else:
                print("Congratulation, X won!")
            break
        if turn == 9:
            print("Draw!")


        #insert x/o
        while True:
            pos = input("It's " + player + " turn.Please insert your pos: ")
            try:
                if int(pos) in range(0,9) and table[int(pos)] == str(pos):
                    table[int(pos)] = player
                    if player == "x":
                        player = "o"
                    elif player == "o":
                        player = "x"
                    break
                else:
                    print("you position isn't right")
                    pass
            except:
                print("you entered wrong key")
                pass
    #restart game?
    while True:
        restart = input("Restart game?(y/n):")
        if restart == "y":
            for x in range(0,9):
                table[x] = str(x)
            playOX()
        elif restart == "n":
            print("Thank you for playing!")
            break
        else:print("You entered wrong key")
if __name__ == "__main__":
    playOX()