import easygui as gui
MENU = """
---Меню---
1. Добавить статистику игры
2. Показать общую статистику
3. Найти лучшую игру
4. Показать все игры (таблица)
5. Рейтинг эффективности
6. Сохранить данные
7. Выход из программы"""



def efficiency_rating(player_name, goals_list, assists_list, penalty_list, games_num):               # Рейтинг эффективноти 5
    if len(goals_list) == 0:
        gui.msgbox("Статитика пута")
        return
    
    total_goals = sum(goals_list)
    total_assists = sum(assists_list)
    total_points = total_goals + total_assists
    total_penalty = sum(penalty_list)
    
    total_games = len(games_num)
    
    coff = total_points / total_games
    
    rating = f'''
    Рейтинг эффективности
    Игрок:{player_name}
    Всего очков-{total_points}
    Всего штрафных минут-{total_penalty}
    '''
    
    gui.msgbox(rating)
    
    if total_penalty == 0:
        gui.msgbox("Штрафных минут нет, дисциплина идеальная")
    else:
        eff = total_points / total_penalty
        
        indicator = f'''
Рейтинг эффективности(очки/штраф):{eff}
'''
         
        if eff < 1:
            indicator += "Старайся набирать больше очков или меньше нарушать правила\n"
            
        elif eff >= 1 and eff < 3:
            indicator += "Хороший показатель,полезный игрок\n"
            
        else:
            indicator += "Отличный результат, звезда команды\n"
            
        
        indicator += f"Средние количество очков за игру-{coff:.2f}"
    
        gui.msgbox(indicator)
    





def add_game_state(player_name, games_num, goals_list, assists_list, penalty_list, time_on_ice):
   
   
    # global player_name
    
    
    if not player_name:
        player_name  = gui.enterbox("Введмте имя игрока: ")
    fieldNames = ["Номер игры: ", "Забитые голы: ", "Голевые передачи: ",  "Штрафные минуты: ", "Время на льду: "]
    fieldValues = []
    fieldValues = gui.multenterbox(f"---Ввод статистики для {player_name}---", fields=fieldNames)

    game_num = int(fieldValues[0])
    goals= int(fieldValues[1])
    assists= int(fieldValues[2])
    penalty= int(fieldValues[3])
    toi= float(fieldValues[4])

    if goals < 0 or assists < 0 or penalty < 0 or  toi < 0:
        gui.msgbox("Ошибка: значение не могут быть отрицательными ")
        return

# Добовление в спски
    games_num.append(game_num)
    goals_list.append(goals)
    assists_list.append(assists)
    penalty_list.append(penalty)
    time_on_ice.append(toi)
    gui.msgbox("Данные успешно добавлены ")
    




def shoy_summary(player_name, goals_list, assists_list, penalty_list, time_on_ice, games_num):
    if len(goals_list) == 0 or len(assists_list) == 0 or len(penalty_list) == 0 or len(time_on_ice) == 0:
        gui.msgbox("Статистика пуста")
        return

    total_goals = sum(goals_list)
    total_assists = sum(assists_list)
    total_points = total_goals + total_assists
    total_penalty = sum(penalty_list)
    avg_toi = round(sum(time_on_ice)/len(time_on_ice),2)
    
    statistics = f'''
    ОБЩАЯ СТАТИСТИКА: {player_name}
    Игры сыграно: {len(games_num)}
    Всего голов: {total_goals}
    Всего передач: {total_assists}
    Всего очков: {total_points}
    Всего штрафных минут: {total_penalty}
    Среднее время на льду: {avg_toi}
    '''
   
    gui.msgbox(statistics)


def best_game(goals_list, assists_list, games_num):                       # Лучшая игра  3
    if len(goals_list) == 0:
        gui.msgbox("Статистика пуста")
        return
    
    max_index = 0
    max_val = goals_list[max_index] + assists_list[max_index]
    
    for i in range(1, len(goals_list)):
        current_val = goals_list[i] + assists_list[i]
        if current_val > max_val:
            max_val = current_val
            max_index = i


    rez = f'''
    Лучшая игра была под номером: {games_num[max_index]}
    Результат: {goals_list[max_index]} голов и {assists_list[max_index]} передач
    Всего очков в матче: {max_val}
    '''

    gui.msgbox(rez)



def show_all_table(games_num, goals_list, assists_list, penalty_list, time_on_ice):                  # Показать все игры таблицей 4
    if len(games_num) == 0:
        gui.msgbox("Список пуст") 
        return
    
    games_list = f'''
Список всех игр
{'№':<5} {'голы':<6} {'передачи':<10} {'штраф(в минутах)':<17} {'время на льду(в минутах)':<25}
------------------------------------------------------
'''
    
    for i in range(len(games_num)):
        games_list += f"{games_num[i]:<5} {goals_list[i]:<6} {assists_list[i]:<10} {penalty_list[i]:<17} {time_on_ice[i]:<25}\n"
     
    gui.msgbox(games_list)
 
    
    
    
    
def hello():
    gui.msgbox("Добропожаловать в Hockey Stats Tracker! ")
    
    
def show_menu():
    gui.msgbox(MENU)
    
    
    
