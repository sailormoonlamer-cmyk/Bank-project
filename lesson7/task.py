def calculate_player_points(goals, assists):
   return goals + assists 

# print(calculate_player_points(5, 3))

def average_points_per_game(total_points, games_played):
    if games_played == 0:
        return 0

    return round(total_points / games_played, 2)

# print(average_points_per_game(5, 0))
    
def get_position_by_number(player_number):
    
    if player_number >= 1 and player_number <=30:
        return "Вратарь"
    elif player_number >= 31 and player_number <= 60:
        return "Защитник"
    elif player_number >=61 and player_number <= 98:
        return "Нападающий"
    else:
        return "Неизвестная позиция!"
    
print(get_position_by_number(100))
