def preprocess(FILE):
    """
    Read from file, return a int matrix surrounded by 0. 
    """
    ret = []
    with open(FILE) as f:
        for line in f:
            line = line[:-1]
            ret.append([(int)(arg) for arg in line.split(' ')])
    ret.insert(0, [0 for _ in range(2 + len(ret[0]))])
    for i in range(1, len(ret)):
        ret[i].insert(0, 0)
        ret[i].append(0)
    ret.append([0 for _ in range(len(ret[0]))])
    return ret

def myRange(x1, x2):
    if (x1 < x2):
        return range(x1, x2)
    else:
        return range(x2, x1)

def direct(board, pos1, pos2):
    if pos1[0] == pos2[0]:
        # print range(pos1[1] + 1, pos2[1])
        for i in myRange(pos1[1] + 1, pos2[1]):
            if board[pos1[0]][i] != 0:
                return False
        return True
    elif pos1[1] == pos2[1]:
        # print range(pos1[0] + 1, pos2[0])
        for i in myRange(pos1[0] + 1, pos2[0]):
            # print (i, pos2[1])
            if board[i][pos1[1]] != 0:
                return False
        return True
    else:
        return False

def oneCorner(board, pos1, pos2):
    if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
        return False
    else:
        return (board[pos1[0]][pos2[1]] == 0 and direct(board, pos1, (pos1[0], pos2[1])) and direct(board, pos2, (pos1[0], pos2[1]))) or\
                 (board[pos2[0]][pos1[1]] == 0 and direct(board, pos1, (pos2[0], pos1[1])) and direct(board, pos2, (pos2[0], pos1[1])))

def twoCorners(board, pos1, pos2):
    for col in range(len(board[0])):
        if board[pos1[0]][col] == 0 and direct(board, (pos1[0], col), pos1) and oneCorner(board, (pos1[0], col), pos2):
            # print 1
            return True
    for row in range(len(board)):
        # 
        if board[row][pos1[1]] == 0 and direct(board, (row, pos1[1]), pos1) and oneCorner(board, (row, pos1[1]), pos2):
            # print (row, pos1[1])
            return True

    for col in range(len(board[0])):
        if board[pos2[0]][col] == 0 and direct(board, (pos2[0], col), pos2) and oneCorner(board, (pos2[0], col), pos1):
            # print 3
            return True
    for row in range(len(board)):
        if board[row][pos2[1]] == 0 and direct(board, (row, pos2[1]), pos2) and oneCorner(board, (row, pos2[1]), pos1):
            # print 4
            return True

    return False


def isConnected(board, pos1, pos2):
    """
    @param: 
        board -- a matrix representing the game
        pos1 -- First Position, e.g. (1, 2)
        pos2 -- Second Position, e.g. (0, 3)
    @return:
        True / False
    """
    
    if board[pos1[0]][pos1[1]] == board[pos2[0]][pos2[1]]:
        return direct(board, pos1, pos2) or oneCorner(board, pos1, pos2) or twoCorners(board, pos1, pos2)
    else:
        return False

def asDict(board):
    ret = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] not in ret:
                ret[board[i][j]] = []
                ret[board[i][j]].append((i, j))
            else:
                ret[board[i][j]].append((i, j))

    return ret


def findSolution(board):
    """
    @param: 
        board -- a matrix representing the game
        i.e.
            0 0 0 0 0 0
            0 1 2 3 4 0
            0 4 2 1 3 0
            0 4 5 4 5 0
            0 0 0 0 0 0
    @return:
        set of valid operations to cancel all items
        i.e. 
            (3, 2), (3, 4), (2, 1), (3, 1), (3, 3), 
            (1, 4), (1, 2), (2, 2), (1, 1), (2, 3), List
            (1, 3), (2, 4)
    """

    while True:
        flag = True
        boardDict = asDict(board)
        for i in boardDict:
            print boardDict[i]
            if len(boardDict[i]) == 2:
                if isConnected(board, boardDict[i][0], boardDict[i][1]):
                    cancelItem(board, boardDict[i][0], boardDict[i][1])
                    flag = False
        if flag:
            break

def cancelItem(board, pos1, pos2):
    x1, y1 = pos1[0], pos1[1]
    x2, y2 = pos2[0], pos2[1]
    board[x1][y1] = 0
    board[x2][y2] = 0
    print pos1, pos2, 'Cancelled'
    print 'New Board: '
    printBoard(board)


def printBoard(board):
    for line in board:
        for arg in line:
            print arg, 
        print 

def main():
    board = preprocess('test.txt')
    printBoard(board)
    
    # for i in asDict(board):
    #     print i, asDict(board)[i]

    pos1 = (1, 1)
    pos2 = (2, 3)
    trans = (1, 2)
    trans2 = (2, 2)
    print pos1, pos2

    print direct(board, pos1, trans)
    print oneCorner(board, trans, pos2)
    print twoCorners(board, trans2, pos2)
    # findSolution(board)


if __name__ == '__main__':
    main()