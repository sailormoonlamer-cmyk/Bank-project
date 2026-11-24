from data import load_data, save_data
from stats import *



games_num = [] # Номер игры
goals_list = [] # Забитые голы
assists_list = [] # Голевые передачи 
penalty_list = [] # Штрафные минуты
time_on_ice = [] # Минуты на льду

player_name = ""

def main():                                                                                                                 # пароль
    hello()
    
    player_name = load_data(games_num, assists_list, penalty_list, time_on_ice, goals_list)
    
    while True:
        show_menu()
        
        choice = gui.enterbox("Выберите пунк с(1-7): ")
        
        if choice == "1":
            add_game_state(player_name, games_num, goals_list, assists_list, penalty_list,time_on_ice)
        elif choice == "2":
            shoy_summary(player_name, goals_list, assists_list,penalty_list, time_on_ice, games_num)
        elif choice == "3":
            best_game(goals_list, assists_list, games_num)
        elif choice == "4":
            show_all_table(games_num, goals_list, assists_list, penalty_list, time_on_ice)
        elif choice == "5":
            efficiency_rating(player_name, goals_list, assists_list,penalty_list, games_num) 
        elif choice == "6":
            save_data(player_name, games_num, goals_list, assists_list, penalty_list, time_on_ice)    
        elif choice == "7":
            save_data(player_name, games_num, goals_list, assists_list, penalty_list, time_on_ice)
            gui.msgbox("Удачи на льду! ")
            break
        else:
            gui.msgbox("Не верный выбор, введи цифры из меню!")
   
            
main()


