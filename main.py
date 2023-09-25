import secrets


def create_board(size):
    return [[" " for _ in range(size)] for _ in range(size)]


def place_mines(board, mines):
    for _ in range(mines):
        x, y = secrets.randbelow(len(board)), secrets.randbelow(len(board))
        board[x][y] = "M"


def reveal_cell(board, x, y):
    if board[x][y] == "M":
        return False
    board[x][y] = "R"
    return True


def mark_mine(board, x, y):
    board[x][y] = "M"


def play_game():
    size = 10
    mines = 10
    board = create_board(size)
    place_mines(board, mines)
    while True:
        x, y = map(int, input("Enter the position to reveal: ").split())
        if not reveal_cell(board, x, y):
            print("Game Over!")
            break
        x, y = map(int, input("Enter the position to mark as mine: ").split())
        mark_mine(board, x, y)


if __name__ == "__main__":
    while True:
        play_game()
        if input("Play again? (y/n)") != "y":
            break
