import random

def roll_dice():
    return random.randint(1, 6)

def move_player(position, dice_value, snakes, ladders):
    new_position = position + dice_value
    if new_position > 100:
        return position  # Stay in the same position if roll exceeds 100
    if new_position in snakes:
        return snakes[new_position]
    elif new_position in ladders:
        return ladders[new_position]
    return new_position

def play_game():
    player1 = 1
    player2 = 1
    turn = 1
    
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}
    
    while True:
        if turn == 1:
            input("Player 1, press Enter to roll the dice...")
            dice_value = roll_dice()
            player1 = move_player(player1, dice_value, snakes, ladders)
            print(f"Player 1 rolled {dice_value} and moved to {player1}")
            if player1 == 100:
                print("Player 1 wins!")
                break
            turn = 2
        else:
            input("Player 2, press Enter to roll the dice...")
            dice_value = roll_dice()
            player2 = move_player(player2, dice_value, snakes, ladders)
            print(f"Player 2 rolled {dice_value} and moved to {player2}")
            if player2 == 100:
                print("Player 2 wins!")
                break
            turn = 1

play_game()
