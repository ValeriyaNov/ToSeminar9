# 3 Создайте программу для игры в "Крестики-нолики".
# Вариант интерфейса:
#  1  |  2 | 3
# --------------
#  4  |  5 | 6
# --------------
#  7  |  8 | 9

import emoji

x = emoji.emojize(':cross_mark:')
o = emoji.emojize(':hollow_red_circle:')
xo = emoji.emojize(':cross_mark::hollow_red_circle:')

board = list(range(1, 10))

print("Введите имя первого игрока - ")
player1 = input()

print("Введите имя второго игрока - ")
player2 = input()


def paint_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)



def take_input(player_token,player1,player2,counter):
   valid = False
   while not valid:
       if counter % 2 == 0:
           player_answer = input(player1 + " куда поставим " + player_token + "? ")
       else:
           player_answer = input(player2 + " куда поставим " + player_token + "? ")
       try:
           player_answer = int(player_answer)
       except:
        print("Некорректный ввод. Попробуйте снова")
        continue
       if player_answer >= 1 and player_answer <= 9:
           if str(board[player_answer-1]) not in xo:
              board[player_answer-1] = player_token
              valid = True
           else:
              print("Эта клетка уже занята!")
       else:
            print("Некорректный ввод. Попробуйте снова")


def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]]== board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False


def main(board):
    counter = 0
    win = False
    while not win:
        paint_board(board)
        if counter % 2 == 0:
           take_input(x,player1,player2,counter)
        else:
           take_input(o,player1,player2,counter)
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              if tmp==x:
                print(player1, "выиграл!")
                win = True
              else:
                print(player2, "выиграл!")
                win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    paint_board(board)

main(board)

input("Нажмите Enter для выхода!")
