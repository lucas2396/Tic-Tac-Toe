if __name__ == '__main__':
    ttt = ""
    winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    game_active=False
    draw=True

    while True:
        if not game_active:
            init=input("Welcome to Tic Tac Toe, enter p to play or q to quit\n")
            if init=="p":
                game_active = True
                count = 0
                player1 = True
                position = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            elif init=="q":
                break
            else:
                print("Wrong choice \n")

        if game_active:
            if draw:
                game_init=True
                count+=1

                if game_init:
                    game_init=False

                if player1:
                    fill_grid="X"
                    player="Player 1"
                    player1=False
                else:
                    fill_grid="0"
                    player = "Player 2"
                    player1=True

            if count==1:
                PlayerInput=input("{} input a position:\n1|2|3\n4|5|6\n7|8|9\n".format(player))
            else:
                PlayerInput = input("{} input a position:".format(player))

            try:
                if position[int(PlayerInput)-1]==" ":
                    position[int(PlayerInput)-1]=fill_grid
                    draw=True
                else:
                    print("position already taken, please try again")
                    draw=False

            except:
                print("Please enter a correct value")
                draw = False

            if draw:
                for i in range(3):
                        for j in range(3):
                            ttt += "|" + position[i*3 +j]
                        ttt+="|\n"
                print(ttt)

                for three in winners:
                    if position[three[0]]==position[three[1]]==position[three[2]] and position[three[0]]!=" ":
                        print("{} won!".format(player))
                        game_active = False

                if count==9 and game_active:
                    print("No one win")
                    game_active = False

