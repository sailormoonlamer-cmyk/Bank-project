

# temp = float(input("Введите температуру "))
# SET_POINT = 22.5

# if temp > SET_POINT:
#     print("Включить охлаждение")
#elif temp > 40:
#     print("Форсировать охдаждение")
# else temp < SET_POINT:
#     print("Включить подогрев")

# LOGIN = "Alex777"
# PASSWORD = "12345"

# login = input("Введите свой логин ")
# password = input("Введите свой пароль ")
# flag = False

# if login == LOGIN and password == PASSWORD:
#     print("Вы успешно вошли в личный кабинет")
#     flag = True
# if flag:
#     print("У вас есть доступ к скачеванию видео")
# elif login == LOGIN and password != PASSWORD:
#     print("Вы не првельно ввели пароль")
# elif password == PASSWORD and login != LOGIN: # logon != LOGIN and password == PASSWORD
#     print("Вы не првельно ввели логин")
# else:
#     print("Неправельный логин или пароль")


# if flag:
#     print("У вас есть доступ к скачеванию видео")
    


# N = 127
# K = int(input("Угадайте число от 1 до 200: "))
# while K != N:
#     K = int(input("Попробуйте еще раз:")) 
# else:
#         print("Вы угадали")
        
# stop = input("Хотите дальше продолжить? ")

# if stop.lower() == "нет":
    
#         print("До новых встреч!")


# игра угадай число

# import random
# import math

# print("""
# Игра угадай число! Компьютер загадывает число, а ты должен его угадать!     
# """)

# min_num = int(input("Введите минимальное число диапазона "))
# max_num = int(input("Введите максимальное число диапазона "))

# secret_num = random.randint(min_num, max_num)
# tries = math.log(max_num - min_num)
# tries = math.ceil(tries)

# print(f"Компьютер загадал число в диапазоне от {min_num} до {max_num}, тебе нужно отгадать за {tries} попыток ")

# while tries > 0:
#     user_num = input("Введите свое число: ") 
#     if not user_num.isdigit():
#         print("Нужно число ввести число!!!")
#         continue
#     user_num = int(user_num)
    
#     if user_num == secret_num:
#         print("Ты угадал!!!")
#         break
#     elif user_num > secret_num:
#       print("Твое число больше чем загадонное!")
    
#     elif user_num < secret_num:
#       print("Твое число меньше чем заганное!")
      
#     tries -= 1
#     print(f"У вас осталось {tries} попыток ")
    
# print("Игра окончена, до новых встреч !!!")



# start = 1

# while start < 6:
#     print(start)
#     start = start + 1

# Цикл for
# for i in range(3, 30, 3):
#     print(i)








#5


# Тип данных список - list - list(), []

# print(list(range(10, 20, 5)))

# a = [] # Пустой список 
# b = list() # Пустой список 

# print(type(b))
    
        #   a = [10, 1.8, True,"Hello" , []] 
# print(a[2]) #  2 - Индекс (True) 
# b = a[0]
# print(b)

# a[2] = False # Замена элементов в списке
# print(a)
# a.append("%") # Добавление новых элементов в список
# print(len(a)) # len счет элементов в списке 

# Методы удаления элементов 
# a.remove("Hello") # Удаление по значению
# print(a)

# a.pop(1) # Удаление по индексу
# print(a)

# for i in a:
#     print(i)

# a = "Hello"

# for i in a:
#     print(i)

# for i, j in enumerate(a): # i-индекс, j-элемент
#      print(i+1, j)


# print("""
# Программа toDoList:  
# Команды для работы:
# 1. Добавить новую запись в список 
# 2. Удалить запись 
# 3. Вывести список задач
# 4. Выйти из программы 
# """)

# toDolist = ["Сходить в магазин", "Встретиться с друзьями"]

# while True:
#     command = input("Выберите команду ->")
#     if not command.isdigit():
#         print("Введите номер команды! ")
#         continue
#     else:
#         command = int(command)

#     if command == 1:
#         new_task = input("Введите название задачи: ")
#         if new_task in toDolist:
#             print("Такая задача есть в списке! ")
#         else:
#             toDolist.append(new_task)
#             print("Задача успешно добавлена!")
    
        
#     elif command == 2:
#         if len(toDolist) == 0:
#             print("Список пуст, удалять нечего!")
#         else:
#             print("Список задач: ")
#             for num, value in enumerate(toDolist):
#                 print(f"{num+1} - {value}")
#             num_task = int(input("Какую задачу вы хотите удалить? "))
#             if num_task in range(1,len(toDolist)+1):
#                 toDolist.pop(num_task-1)
#                 print("Задача удалена ")
#             else:
#                 print("Такой задачи нет! ")
                
    
#     elif command == 3:
#         if len (toDolist) == 0:
#             print("Список пока пуст!")
#         else:
#             print("Список задач: ")
#             for num, value in enumerate(toDolist):
#                 print(f"{num+1} - {value}")
#     elif command == 4:
#         print("До новых встреч!")
#         break
    
#     else:
#         print("Такой команды нет!")



#6 
# import random
# answers = ["Да","Нет","Спроси в другой раз" ]
# # while True:
# #     ask = input("Что ты хочешь узнать?: ")
# #     answer = random.choice(answers)
# #     print(answer)
# #     if ask.lower() in ["хватит","нет","конец","стоп","пока"]:
# #         print("Шар говорит тебя пока! ")
# #         break


# a = answers[-3]
# print(a)



#7
# Функции 
# 1.Обычная функция 

# def - Любая функция 

# Определение функции 
# def calcilate():
#         x = 2 + 5
#         print(x)
        
# Вызов функции 
# calcilate()

# 2. Принимающая функция

# def mul(a, b):
#         c = a * b
#         print(f"Результат умножения - {c}")
        
# mul(10, 55)


# 3. Возвращающая функция 

# def summa(a , b , c):
#         d = a + b + c
#         return d

# # print(summa(10, 100 , 77))
# s = summa(10, 100 , 77)
# print(s)

