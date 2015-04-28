def preprocess():
    """
    Read from file, return a int matrix surrounded by 0. 
    """
    ret = []
    with open('test.txt') as f:
        for line in f:
            line = line[:-1]
            ret.append([(int)(arg) for arg in line.split(' ')])
    ret.insert(0, [0 for _ in range(2 + len(ret[0]))])
    for i in range(1, len(ret)):
        ret[i].insert(0, 0)
        ret[i].append(0)
    ret.append([0 for _ in range(len(ret[0]))])
    return ret

def isConnected(board, pos1, pos2):
    """
    @param: 
        board -- a matrix representing the game
        pos1 -- First Position, e.g. (1, 2)
        pos2 -- Second Position, e.g. (0, 3)
    @return:
        True / False
    """
    def direct(board, pos1, pos2):
        if pos1[0] == pos2[0]:
            for i in range(pos1[1] + 1, pos2[1]):
                if board[pos1[0]][i] != 0:
                    return False
            return True
        elif pos1[1] == pos2[1]:
            for i in range(pos1[0] + 1, pos2[0]):
                if board[i][pos1[0]] != 0:
                    return False
            return True
        else:
            return False

    def oneCorner(board, pos1, pos2):
        if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
            return False
        else:
            return (direct(board, pos1, (pos1[0], pos2[1])) and direct(board, pos2, (pos1[0], pos2[1]))) or\
                     (direct(board, pos1, (pos1[1], pos2[0])) and direct(board, pos2, (pos1[1], pos2[0])))

    def twoCorners(board, pos1, pos2):
        pass


def main():
    ret = preprocess()
    for line in ret:
        for arg in line:
            print arg, 
        print 


if __name__ == '__main__':
    main()