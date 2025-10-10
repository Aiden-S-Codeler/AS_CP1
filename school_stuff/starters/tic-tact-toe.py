#AS JC IB KH 2nd tic tac toe

board_list1 = ["", "", ""]
board_list2 = ["", "", ""]
board_list3 = ["", "", ""]

import random

while True:
    play = int.input("where would you like to place your X? ")
    if play == 1 and board_list1.index(1) == "":
        board_list1.index(1) = "X"
        pass
    elif play == 2 and board_list1.index(2) == "":
        board_list1.index(2) = "X"
        pass
    elif play == 3 and board_list1.index(3) == "":
        board_list1.index(3) = "X"
        pass
    elif play == 4 and board_list2.index(1) == "":
        board_list1.index(1) = "X"
        pass
    elif play == 5 and board_list2.index(2) == "":
        board_list1.index(2) = "X"
        pass
    elif play == 6 and board_list2.index(3) == "":
        board_list1.index(3) = "X"
        pass
    elif play == 7 and board_list3.index(1) == "":
        board_list1.index(1) = "X"
        pass
    elif play == 8 and board_list3.index(2) == "":
        board_list1.index(2) = "X"
        pass
    elif play == 9 and board_list3.index(3) == "":
        board_list1.index(3) = "X"
        pass
    else:
        print("Invalid.")
        continue
    rplay = int.input("where would you like to place your X? ")
    if rplay == 1 and board_list1.index(1) == "":
        board_list1.index(1) = "X"
        pass
    elif rplay == 2 and board_list1.index(2) == "":
        board_list1.index(2) = "X"
        pass
    elif rplay == 3 and board_list1.index(3) == "":
        board_list1.index(3) = "X"
        pass
    elif rplay == 4 and board_list2.index(1) == "":
        board_list1.index(1) = "X"
        pass
    elif rplay == 5 and board_list2.index(2) == "":
        board_list1.index(2) = "X"
        pass
    elif rplay == 6 and board_list2.index(3) == "":
        board_list1.index(3) = "X"
        pass
    elif rplay == 7 and board_list3.index(1) == "":
        board_list1.index(1) = "X"
        pass
    elif rplay == 8 and board_list3.index(2) == "":
        board_list1.index(2) = "X"
        pass
    elif rplay == 9 and board_list3.index(3) == "":
        board_list1.index(3) = "X"
        pass
    else:
        continue