bod = ["0","1","2",
"3","4","5",
"6","7","8"]

def board():
    print(bod[0],'|',  bod[1],'|',  bod[2], '|')
    print('----------------')
    print(bod[3],'|',  bod[4],'|',  bod[5], '|')
    print('----------------')
    print(bod[6],'|',  bod[7],'|',  bod[8], '|')

while True:
    board()
    spot = int(input("choose a spot(x):"))
    bod[spot] = "x"
    """if bod[spot] == "x" or bod[spot] == "o":
        print("---spot taken---")"""
    board()
    spot_two = int(input("choose a spot(o):"))
    bod[spot_two] = "o"
    """if bod[spot] == "x" or bod[spot] == "o":
        print("---spot taken---")"""

        #player_one checks
    if bod[0] == bod[1] == bod[2] =="x":
        print("player one (x) won")
        break
    if bod[3] == bod[4] == bod[5] == "x":
        print("player one (x) won")
        break
    if bod[6] == bod[7] == bod[8] == "x":
        print("player one (x) won")
        break
    if bod[0] == bod[3] == bod[6] == "x":
        print("player one (x) won")
        break
    if bod[1] == bod[4] == bod[7] == "x":
        print("player one (x) won")
        break
    if bod[2] == bod[5] == bod[8] == "x":
        print("player one (x) won")
        break
    if bod[0] == bod[4] == bod[8] == "x":
        print("player one (x) won")
        break
    if bod[6] == bod[4] == bod[2] == "x":
        print("player one (x) won")
        break

    #player_two checks
    if bod[0] == bod[1] == bod[2] =="o":
        print("player two (o) won")
        break
    if bod[3] == bod[4] == bod[5] == "o":
        print("player two (o) won")
        break
    if bod[6] == bod[7] == bod[8] == "o":
        print("player two (o) won")
        break
    if bod[0] == bod[3] == bod[6] == "o":
        print("player two (o) won")
        break
    if bod[1] == bod[4] == bod[7] == "o":
        print("player two (o) won")
        break
    if bod[2] == bod[5] == bod[8] == "o":
        print("player two (o) won")
        break
    if bod[0] == bod[4] == bod[8] == "o":
        print("player two (o) won")
        break
    if bod[6] == bod[4] == bod[2] == "o":
        print("player two (o) won")
        break
    else:
        print("---it is a draw---")