def TicTacDraw(board):
    number_row = len(board)
    for i in range(number_row):
        o = ""
        n = len(board[i])
        for j in range(n):
            if board[i][j] == 0:
                o = o + " O "
            elif board[i][j] == 1:
                o = o + " X "
            elif board[i][j] == 2:
                o = o + "   "

            if j is not (n-1):
                o = o+"|"
        print(o)

        if i is not (number_row-1):
            print("----"*(n-1) + "---")
