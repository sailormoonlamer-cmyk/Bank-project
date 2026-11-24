# 1-Запись в файл - режим записи в файл
# file = open('test_1.txt', 'w', encoding='utf-8')
# file.write("Hello\n")
# file.write('World')
# file.close()


# 2-Режим добовления в файл информации 
# f = open('test_1.txt', 'a', encoding='utf-8')
# for i in 'LOGIN':
#     f.write(f'\n{i}')
# f.close()


# 3-Режим чтения из файла
# f = open('test_1.txt', 'r', encoding='utf-8')
# data = f.readlines()
# f.close()


# print(data)


# Контекстый менеджер with 

# with open('test_1.txt', 'a', encoding='utf-8') as f:
#     data = f.read()
    
#     print(data)




# from random import randint

# def creat_number(file_name):
#     with open(file_name, 'w', encoding= 'utf-8') as f:              #название,режим,кодировка
#         for i in range(10):
#             num = randint(1, 100)
#             f.write(f'{num}\n')
#         print('Файл создан и числа записаны!')
        
        
# # # creat_number('number.txt')


# def read_number(file_name):
#     with open(file_name, 'r', encoding= 'utf-8') as f:
#         data = f.read().split('\n')
#         data.pop(-1)
#         for i, j in enumerate(data):
#             data[i] = int(j) 
#         return data

# # new = read_number('number.txt')
# # print(new) 

# def safe_sort(spisok, file_name):
#     with open(file_name, 'w', encoding= 'utf-8') as f:
#         for i in spisok:
#             if i % 2 == 0:
#                 f.write(f"{i}\n")
#         print("Файл создан с четными числами!")
        

# safe_sort(read_number("number.txt"), "even.txt")


a = []
b = []
c = []
d = []
e = []




def load():
    with open("статистика.txt", 'r', encoding= 'utf-8') as f:
        data = f.readlines()
        player = data[0].strip()
        print(player)
        for i in range(1, len(data)):
            line = data[i].strip()
            parts = line.split(',')
            print(parts)
            a.append(int(parts[0]))
            b.append(int(parts[1]))
            c.append(int(parts[2]))
            d.append(int(parts[3]))
            e.append(float(parts[4]))
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)

load()      

        
            




