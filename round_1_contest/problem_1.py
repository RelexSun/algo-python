def chessBoard(x, y):
    if (x + y) % 2 == 0:
        return 'black'
    else:
        return 'white'

x, y = input().split()
x, y = int(x), int(y)
print(chessBoard(x, y))