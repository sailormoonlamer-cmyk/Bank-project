print("""
Программа toDoList:  
Команды для работы:
1. Добавить новую запись в список 
2. Удалить запись 
3. Вывести список задач
4. Выйти из программы 
""")

toDolist = ["Сходить в магазин", "Встретиться с друзьями"]



def showToDolist(a):
    print("Список задач: ")
    for num, value in enumerate(a):
        print(f"{num+1} - {value}")

def addToDolist(task, spisok):
    if task in spisok:
        print("Такая задача есть в списке! ")
    else:
        spisok.append(task)
        print("Задача успешно добавлена!")

def dellTask(task, spisok):
    if task in range(1,len(spisok)+1):
        toDolist.pop(task-1)
        print("Задача удалена ")
    else:
        print("Такой задачи нет! ")

while True:
    command = input("Выберите команду ->")
    if not command.isdigit():
        print("Введите номер команды! ")
        continue
    else:
        command = int(command)

    if command == 1:
        new_task = input("Введите название задачи: ")
        addToDolist(new_task, toDolist)
        
    elif command == 2:
        if len(toDolist) == 0:
            print("Список пуст, удалять нечего!")
        else:
            showToDolist(toDolist)
            num_task = int(input("Какую задачу вы хотите удалить? "))
            dellTask(num_task, toDolist)
                
    elif command == 3:
        if len (toDolist) == 0:
            print("Список пока пуст!")
        else:
            showToDolist(toDolist)
    elif command == 4:
        print("До новых встреч!")
        break
    
    else:
        print("Такой команды нет!")


# def concat(word, count):
#     return word * count

# res = concat("?", 10)
# print(res)