import tkinter as tk
import random

def draw_board(board, buttons):
    for i, button in enumerate(buttons):
        button.config(text=board[i])

def get_user_move(buttons, player_symbol):
    for i, button in enumerate(buttons):
        if button['text'] == ' ':
            button.config(state=tk.NORMAL, command=lambda i=i: button_click(i, player_symbol, buttons))
        else:
            button.config(state=tk.DISABLED)

def get_computer_move(board):
    available_indices = [i for i, value in enumerate(board) if value == ' ']
    return random.choice(available_indices)

def button_click(index, player_symbol, buttons):
    global board
    buttons[index].config(text=player_symbol, state=tk.DISABLED)
    board[index] = player_symbol
    winner = check_winner(board)
    if winner:
        if winner == player_symbol:
            print('Kazandın!')
        elif winner == 'Tie':
            print('Berabere!')
        else:
            print('Kaybettin!' if player_symbol == 'X' else 'Kazandın!')
        root.quit()
        return
    computer_move = get_computer_move(board)
    buttons[computer_move].config(text='O' if player_symbol == 'X' else 'X', state=tk.DISABLED)
    board[computer_move] = 'O' if player_symbol == 'X' else 'X'
    winner = check_winner(board)
    if winner:
        if winner == player_symbol:
            print('Kazandın!')
        elif winner == 'Tie':
            print('Berabere!')
        else:
            print('Kaybettin!' if player_symbol == 'O' else 'Kazandın!')
        root.quit()
        return

def check_winner(board):
    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]

    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]

    # check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]

    # check for tie
    if ' ' not in board:
        return 'Tie'

    return None

def play_game():
    global board
    board = [' '] * 9

    # create the GUI
    global root
    root = tk.Tk()
    root.title("Tic Tac Toe")

    player_symbol = tk.StringVar(value='X')
    tk.Label(root, text='Select your symbol:', font=('Arial', 14)).grid(row=0, columnspan=3)
    tk.Radiobutton(root, text='X', variable=player_symbol, value='X',
                   font=('Arial', 14), command=lambda: get_user_move(buttons, player_symbol.get())).grid(row=1, column=0)
    tk.Radiobutton(root, text='O', variable=player_symbol, value='O',
                   font=('Arial', 14), command=lambda: get_user_move(buttons, player_symbol.get())).grid(row=1, column=1)
    buttons = []
    for i in range(9):
        button = tk.Button(root, text=' ', font=('Arial', 20), width=4, height=2, state=tk.DISABLED)
        button.grid(row=i//3+2, column=i%3)
        buttons.append(button)

    root.protocol('WM_DELETE_WINDOW', root.quit)

    root.mainloop()

if __name__ == '__main__':
    play_game()
