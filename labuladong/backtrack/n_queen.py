"""N皇后问题"""

res = []


def isValid(board, row, col):
    n = len(board)

    for i in range(n):
        if board[i][col] == 'Q':
            return False

    for i in range(row, -1, -1):
        for j in range(col, n):
            if board[i][j] == 'Q':
                return False

    for i in range(row, -1, 1):
        for j in range(col, -1, -1):
            if board[i][j] == 'Q':
                return False


def main(N):
    board = [0 for i in range(N)]
    backtrack(board, 0)
    return res


def backtrack(board, row):
    if len(board) == row:
        res.append(board)
        return

    n = len(board[row])
    for col in range(n):
        if not isValid(board, row, col):
            continue
        board[row][col] = 'Q'
        backtrack(board, row + 1)
        board[row][col] = 0
