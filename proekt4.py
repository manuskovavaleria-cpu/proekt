def start_game():
    sticks = 21
    turn = input("Хотите ходить первыми? (Да/Нет): ").strip().lower()
    if turn == 'да':
        human_first = True
    else:
        human_first = False
    play_game(human_first, sticks)
def human_turn(sticks_left):
    while True:
        try:
            take = int(input(f"Ваш ход. Осталось {sticks_left} спичек. Сколько возьмёте (1-3)? "))
            if 1 <= take <= min(3, sticks_left):
                return take
            else:
                print("Ошибка! Можно взять от 1 до 3 спичек.")
        except ValueError:
            print("Ошибка! Введите целое число.")
def computer_turn(sticks_left):
    if sticks_left >= 4 and sticks_left % 4 != 0:
        comp_take = sticks_left % 4
    else:
        comp_take = random.randint(1, min(3, sticks_left))
    print(f"Компьютер берет {comp_take} спичек.")
    return comp_take
def check_winner(sticks_left):
    if sticks_left == 0:
        return True
    return False
def play_game(human_first, sticks):
    current_player = human_first
    while sticks > 0:
        if current_player:
            taken = human_turn(sticks)
        else:
            taken = computer_turn(sticks)
        sticks -= taken
        current_player = not current_player
        if check_winner(sticks):
            winner = "Вы победили!" if current_player else "Победил компьютер!"
            print(winner)
            break
if __name__ == "__main__":
    import random
    start_game()
