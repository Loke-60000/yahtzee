from main import *
from collections import Counter
from itertools import combinations

def calculate_mission_major(dice_values, round_number):
    frequency = Counter(dice_values)
    most_common_num, count = frequency.most_common(1)[0]
    """Calculate points based on the most common dice value and Yahtzee missions."""
    if round_number > 6:
        if count == 5:
            # Yahtzee (5 same dices)
            return 50
        elif count == 4:
            # Carré (4 same dices)
            return sum(dice_values)
        elif count == 3 and len(frequency) == 2:
            # Full (3 same dices and 2 other same dices)
            return 25
        elif count == 3:
            # Three of a kind
            return sum(dice_values)
        elif is_sequence(dice_values, 5):
            # Large straight (any sequence of 5 numbers)
            return 40
        elif is_sequence(dice_values, 4):
            # Small straight (any sequence of 4 numbers)
            return 30
        return 0
    else:
        # Additional logic if needed for rounds <= 6
        return most_common_num * count

def is_sequence(dice_values, length):
    """Check if there is a sequence of a certain length in the dice values."""
    dice_values = sorted(set(dice_values))  # Remove duplicates and sort
    for i in range(len(dice_values) - length + 1):
        if dice_values[i + length - 1] - dice_values[i] == length - 1:
            return True
    return False

    
    
#     max_score = max(scores.values())
#     for player, score in scores.item():
#         if score == max_score:
#             return print(f'{player} is the winner of the game')
    

   
# def score_bonus():
#     if score >= 65 and round == 6:
#        score += 35
#     return(score)

# def select_best_option():
    
# def low_suit():
#     for sequence in dice_values(range(1,6), 4):
#         return 30
    
# def great_suit():
#     for sequence in dice_values(range(1,6), 5):
#         return 40
    
       
       
    
    
    