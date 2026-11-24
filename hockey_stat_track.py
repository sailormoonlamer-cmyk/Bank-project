



# Глобальные списки для хранения статистики 
games_num = [] # Номер игры
goals_list = [] # Забитые голы
assists_list = [] # Голевые передачи 
penalty_list = [] # Штрафные минуты
time_on_ice = [] # Минуты на льду

player_name = ""
FILENAME = "статистика.txt"

def add_game_state():
    global player_name
    
    
    if not player_name:
        player_name  = input("Введмте имя игрока: ")

    print(f"---Ввод статистики для {player_name}---")

    game_num = int(input("Номер игры: "))
    goals= int(input("Забитые голы: "))
    assists= int(input("Голевые передачи: "))
    penalty= int(input("Штрафные минуты: "))
    toi= float(input("Время на льду: "))

    if goals < 0 or assists < 0 or penalty < 0 or  toi < 0:
        print("Ошибка: значение не могут быть отрицательными ")
        return

# Добовление в спски
    games_num.append(game_num)
    goals_list.append(goals)
    assists_list.append(assists)
    penalty_list.append(penalty)
    time_on_ice.append(toi)
    print("Данные успешно добавлены ")
    
def shoy_summary():
    if len(goals_list) == 0 or len(assists_list) == 0 or len(penalty_list) == 0 or len(time_on_ice) == 0:
        print("Статистика пуста")
        return

    total_goals = sum(goals_list)
    total_assists = sum(assists_list)
    total_points = total_goals + total_assists
    total_penalty = sum(penalty_list)
    avg_toi = sum(time_on_ice)/len(time_on_ice)
    
    print("="*30)
    print(f"ОБЩАЯ СТАТИСТИКА: {player_name}")
    print(f"Игры сыграно: {len(games_num)}")
    print(f"Всего голов: {total_goals}")
    print(f"Всего передач: {total_assists}")
    print(f"Всего очков: {total_points}")
    print(f"Всего штрафных минут: {total_penalty}")
    print(f"Среднее время на льду: {avg_toi}")
    print("="*30)
    
    
    
    
    
def best_game():                       # Лучшая игра  3
    if len(goals_list) == 0:
        print("Статистика пуста")
        return
    
    max_index = 0
    max_val = goals_list[max_index] + assists_list[max_index]
    
    for i in range(1, len(goals_list)):
        current_val = goals_list[i] + assists_list[i]
        if current_val > max_val:
            max_val = current_val
            max_index = i

    print(f"Лучшая игра была под номером: {games_num[max_index]}")    
    print(f"Результат: {goals_list[max_index]} голов и {assists_list[max_index]} передач") 
    print(f"Всего очков в матче: {max_val}")

        
    
    
    
def show_all_table():                  # Показать все игры таблицей 4
    if len(games_num) == 0:
        print("Список пуст") 
        return
    
    print("Список всех игр")
    print(f"{'№':<5} {'голы':<6} {'передачи':<10} {'штраф(в минутах)':<17} {'время на льду(в минутах)':<25}")
    print("-" * 70)
    for i in range(len(games_num)):
        print(f"{games_num[i]:<5} {goals_list[i]:<6} {assists_list[i]:<10} {penalty_list[i]:<17} {time_on_ice[i]:<25} ")
    print("-" * 70)  
    
        
def efficiency_rating():               # Рейтинг эффективноти 5
    if len(goals_list) == 0:
        print("Статитика пута")
        return
    
    total_goals = sum(goals_list)
    total_assists = sum(assists_list)
    total_points = total_goals + total_assists
    total_penalty = sum(penalty_list)
    
    total_games = len(games_num)
    
    coff = total_points / total_games
    print("Рейтинг эффективности")
    print(f"Игрок:{player_name} ")
    print(f"Всего очков-{total_points}")
    print(f"Всего штрафных минут-{total_penalty}")
    
    if total_penalty == 0:
        print("Штрафных минут нет, дисциплина идеальная")
    else:
        eff = total_points / total_penalty
        print(f"Рейтинг эффективности(очки/штраф):{eff}")
        if eff < 1:
            print("Старайся набирать больше очков или меньше нарушать правила")
        elif eff >= 1 and eff < 3:
            print("Хороший показатель,полезный игрок")
        else:
            print("Отличный результат, звезда команды")
        
    print(f"Средние количество очков за игру-{coff:.2f}")
    
    print("-" * 70)
  
  
  
    
    
def save_data():
    global player_name
    if len(games_num) == 0:
        print("Ошибка! сначала добавьте игру!")
        with open(FILENAME, "w", encoding="utf-8") as file:
            file.write("")
        return
    
        
    
    with open(FILENAME, "w", encoding="utf-8") as file:
        file.write(player_name + "\n")
        
        for i in range(len(games_num)):
            line = f"{games_num[i]},{goals_list[i]},{assists_list[i]},{penalty_list[i]},{time_on_ice[i]}"
            file.write(line +"\n")
              
    print(f"данные успешно сохранены в файл '{FILENAME}'") 





   




def load_data():
    global player_name, games_num, assists_list, penalty_list, time_on_ice, goals_list
    with open("статистика.txt", 'r', encoding= 'utf-8') as f:
        data = f.readlines()
        player_name = data[0].strip()
      
        for i in range(1, len(data)):
            line = data[i].strip()
            parts = line.split(',')
            if len(parts) == 5:
                games_num.append(int(parts[0]))
                goals_list.append(int(parts[1]))
                assists_list.append(int(parts[2]))
                penalty_list.append(int(parts[3]))
                time_on_ice.append(float(parts[4]))
            else:
                print(f"Предупреждение: строка {i+1} повреждена или пропущена ")
        if len(games_num) > 0:
            print(f"Данные загружены для игрока: {player_name}")
            print(f"Загруженно игр: {len(games_num)}")
            
        else:
            print("В файле не найденно данных об играх")
  

        
        
        
         
                                                             
    
    
    
def main():
    print("Добропожаловать в Hockey Stats Tracker! ")
    
    load_data()
    
    while True:
        print("---Меню---")
        print("1. Добавить статистику игры")
        print("2. Показать общую статистику")
        print("3. Найти лучшую игру")
        print("4. Показать все игры (таблица)")
        print("5. Рейтинг эффективности")   
        print("6. Сохранить данные")
        print("7. Выход из программы")
        
        choice = input("Выберите пунк с(1-7): ")
        
        if choice == "1":
            add_game_state()
        elif choice == "2":
            shoy_summary()
        elif choice == "3":
            best_game()
        elif choice == "4":
            show_all_table()
        elif choice == "5":
            efficiency_rating() 
        elif choice == "6":
            save_data()
        elif choice == "7":
            save_data()
            print("Удачи на льду! ")
            break
        else:
            print("Не верный выбор, введи цифры из меню!")
   
            
main()
