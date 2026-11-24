import easygui as gui





FILENAME = "lesson11\lesson8\статистика.txt"





def save_data(player_name, games_num, goals_list, assists_list, penalty_list, time_on_ice):
    if len(games_num) == 0:
        gui.msgbox("Ошибка! сначала добавьте игру!")
        with open(FILENAME, "w", encoding="utf-8") as file:
            file.write("")
        return
    
        
    
    with open(FILENAME, "w", encoding="utf-8") as file:
        file.write(player_name + "\n")
        
        for i in range(len(games_num)):
            line = f"{games_num[i]},{goals_list[i]},{assists_list[i]},{penalty_list[i]},{time_on_ice[i]}"
            file.write(line +"\n")
              
    gui.msgbox(f"данные успешно сохранены в файл '{FILENAME}'") 




def load_data(games_num, assists_list, penalty_list, time_on_ice, goals_list):
    # global player_name
    with open(FILENAME, 'r', encoding= 'utf-8') as f:
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
                gui.msgbox(f"Предупреждение: строка {i+1} повреждена или пропущена ")
        if len(games_num) > 0:
            gui.msgbox(f"Данные загружены для игрока: {player_name}")
            gui.msgbox(f"Загруженно игр: {len(games_num)}")
            
        else:
            gui.msgbox("В файле не найденно данных об играх")
        
        return player_name