from functions import *
import colorama
colorama.init(autoreset = True)

show_board(al)
cm = 0
x_moves = 0
moves = 0
cdd = 3
played = []

while True:
    if chkfin(check_winner):
        ipx = finwhr(check_winner)
    elif chksav(check_winner):
        ipx = savwhr(check_winner)
    elif x_moves < cdd:
        ipx = computer_moves[cm][x_moves]
    else:
        ipx = av[0]
    print("Computer ")
    excuteinpx(ipx, c1mx, c2mx, al)
    played.append(ipx)
    x_moves += 1
    moves += 1
    avmov(av, al)
    show_board(al)
    if check_win(check_winner, winner):
        break
    if moves == 9:
        break


    #User
    while True:
        ipo = int(input("Enter the position for O: "))
        if ipo in played:
            print("Invalid Input")

        else:
            break


    excuteinpo(ipo, c1mo, c2mo, al)
    played.append(ipo)

    while x_moves == 1:
        if ipo == 2 or ipo == 3:
            cm = 0
            break
        if ipo == 4 or ipo == 7:
            cm = 1
            break
        if ipo == 5:
            cm = 2
            cdd = 2
            break
        if ipo == 6 or ipo == 9:
            cm = 3
            break
        if ipo == 8:
            cm = 4
            break
    moves += 1
    avmov(av, al)
    if check_win(check_winner, winner):
        break
    show_board(al)

if len(winner) == 1 and winner[0] == Fore.LIGHTRED_EX + Style.BRIGHT + "X":
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "Computer WON!")
elif len(winner) == 1 and winner[0] != Fore.LIGHTRED_EX+ Style.BRIGHT + "X":
    print(Fore.LIGHTRED_EX+ Style.BRIGHT + "You WON!")
else:
    print(Fore.LIGHTRED_EX + Style.BRIGHT + "D" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "R" + Fore.LIGHTRED_EX + Style.BRIGHT + "A" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "W")
    