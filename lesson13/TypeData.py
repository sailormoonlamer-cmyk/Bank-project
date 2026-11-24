



# num = 10.0

# word = 'Hello'

# a = True


# spisok = [num, word, a]          # список


# # тип данных кортеж - tuple 

# # var1 = tuple()
# # var2 = ('dfk', 10, 10.6)       #картеж
# # print(type(var1))
# # print(var2)
# # a = var2[1]
# # print(a)
# # var2[2] = 5
# # var3 = list(var2)
# # var3.append('kdfj')
# # var4 = tuple(var3)
# # # print(len(var2))
# # # print(var2.count(10))
# # for i, j in enumerate(var2):
# #     print(i, j)
    
    
    
# # дип данных словарь - dict
# # dict1 = dict()
# dict2 = {'key1':10, 'key2':10.7, 1:True}
# # print(len(dict2))
# dict2['key2'] = 'World'  # изменение значения по ключу
# dict2['key3'] = False    # добовление нового ключа и его значение 
# # print(dict2)
# b = dict2.keys()
# c = dict2.values()
# # for i in dict2:
#     # print(i, dict2[i])
    
# # for i, j in dict2.items():
# #     print(i, j)

# # взять значение по не существующему ключу
# # d = dict2['key4']
# # d = dict2.get('key4', 'Такого ключа не существует')
# # print(d)

# # преобразование словаря в кортеж/список
# # e = tuple(dict2.items())
# # e2 =list (dict2.items())
# # print(e2)

# # f = (('key1', 10), ('key2', 'World'), (1, True), ('key3', False))
# # g = dict(f)
# # print(g)


# # генератор списка 

# a = [i for i in range(100, 200 , 10)]
# print(a)






# Логи посещений: (пользователь, дата)
logs = [
    ("alice", "2025-05-01"),
    ("bob", "2025-05-01"),
    ("alice", "2025-05-02"),
    ("charlie", "2025-05-02"),
    ("alice", "2025-05-02"),   # повтор в тот же день
    ("bob", "2025-05-03"),
]

# Корзина: {товар: (цена, количество)}
basket = {
    "ноутбук": (50000, 1),
    "мышь": (1500, 2),
    "клавиатура": (3000, 1),
}

# Прайс-лист и остатки на складе
price = {"яблоки": 120, "бананы": 80, "лимоны": 150, "апельсины": 90}
stock = {"яблоки": (50, "кг"), "бананы": (30, "кг"), "апельсины": (20, "кг")}

# Голосование за фильмы: (фильм, оценка 1-5)
votes = [
    ("Дюна", 5), ("Барби", 5), ("Оппенгеймер", 5),
    ("Дюна", 4), ("Барби", 5), ("Дюна", 5),
]

# Контакты: (имя, телефон)
contacts = [
    ("Анна", "+7-999-123-45-67"),
    ("Борис", "+7-999-76-54-321"),
    ("Алексей", "+7-999-11-22-333"),
    ("Алина", "+7-999-88-77-66"),
]



# def user_activity(logs):
    
#     activity = {}
    
#     for user, date in logs:
#         if user not in activity:
#             activity[user] = []
#     # print(activity)
#         if date not in activity[user]:
#             activity[user].append(date)

           
            
            
            
#     return activity

# clean_data = user_activity(logs)
# print(clean_data)




# def check_basket(basket):
    
#     total = 0
    
#     for item, (price,qty) in basket.items():
#         cost = price * qty
         
#         total += cost  
        
#         print(f'{item} {qty} x {price} = {cost}руб') 
#     print(f'ИТОГО:{total}руб')
    
# check_basket(basket)
    
    

# def group_contacts(contacts):
    
#     group = {}
    
#     for name, phone in contacts:
#         letter = name[0].upper()
        
#         if letter not in group:
#             group[letter] = []
            
#         group[letter].append((name,phone))
    
    
#     return group


# print(group_contacts(contacts)['А'])




# def merge_inventory(price, stock):
#     result = {}
#     total_price = 0
    
    
#     for item in price:
#         if item in stock:
            
#             item_price = price[item]
#             quantity, unit  = stock[item]
            
#             result[item] = (item_price, quantity, unit)
            
#             total_price = total_price + item_price * quantity
            
#     print(result)
#     print(f'Общая стоимость склада:{total_price}руб')
     
#     return result


# merge_inventory(price, stock)








# def movie_rating(votes):
#     rating_data = {}
#     for film, score in votes:
#         if film not in rating_data:
#             rating_data[film] = [0, 0]
#         rating_data[film][0] += score
#         rating_data[film][1] += 1
#     # print(rating_data)
#     result = {}
    
#     for film, (total, count) in rating_data.items():
#         if count > 0:
#             avg = round(total / count, 2)
            
#             result[film] = (avg, count)
            
  
    
#     best_film = None 
#     best_count = count
#     best_avg = 0 
    
#     for film, (avg, count) in result.items():
#         if avg > best_avg:
#             best_avg = avg
#             best_film = film
            
#         elif avg == best_avg and count > best_count:
#             best_count = count
#             best_film = film
            
     
            
#     return result, (best_film, best_avg, best_count)
    
    

# print(movie_rating(votes))





# def is_palindrome(text):
#     clean = ""
#     for i in text.lower():
#         clean += i 
    
#     for i in range(len(clean)//2):
#         if clean[i] != clean[-1-i]:
#             return False
#     return True
        
        
# print(is_palindrome('пайтон'))

















# def char_frequency(text):
#     quantity = {}
    
#     for ch in text:
#         quantity[ch] = quantity.get(ch, 0) + 1
    
#     return quantity

# print(char_frequency('ho use'))



# def char_frequency(text):
#     quantity = {}
#     for i in text:
#         if i in quantity:
#             quantity[i] += 1
#         else:
#             quantity[i] = 1
#     return quantity

# print(char_frequency('ho use e'))








    
    
    

    
# def remove_duplicates(lst):
#     result = []
    
#     for i in lst:
#         if i not in result:
#             result.append(i)
    
#     return result
    
# lst = [1, 2, 2, 3, 1, 4, 2]
        
# print(remove_duplicates(lst))



# def find_index(items, target):
#     for i in range(len(items)):
#         if items[i] == target:
#             return i
#     return -1


# print(find_index('word', "?"))

# def count_items(items):
#     count = 0
#     for item in items:
#         count += 1
#     return count


# def find_best(items, key_func):
#     if not items:
#         return None
#     best = items[0]
#     best_score = key_func(best)
#     for item in items[1:]:
#         score = key_func(item)
#         if score > best_score:
#             best = item
#             best_score = score
#     return best




# word = [ 'орех', 'дуб', 'груша' ]

# print(find_best(word, count_items))








# def spend_by_category(transactions):
#     freq = {}
#     for cat, amount in transactions:
#         if cat in freq:
#             freq[cat] += amount
#         else:
#             freq[cat] = amount
#     return freq



# print(spend_by_category([("еда", 350), ("транспорт", 150), ("еда", 200), ("кафе", 500), ("транспорт", 50)]))




# def are_anagrams(word1, word2):
    
#     if len(word1) != len(word2):
#         return False
#     # quantity1 = {}
#     # for char in word1:
#     #     if char in quantity1:
#     #         quantity1[char] +=1
#     #     else:
#     #         quantity1[char] = 1
            
#     # quantity2 = {}
#     # for char in word2:
#     #     if char in quantity2:
#     #         quantity2[char] +=1
#     #     else:
#     #         quantity2[char] = 1
            
#     # return quantity1 == quantity2
#     return char_frequency(word1) == char_frequency(word2)   

# print(are_anagrams('комок', 'комок'))
    
        


# def common_friends(list1, list2):
#     result = []
#     for name in list1:
#         if name in list2 and name not in result:
#             result.append(name)
            
#     return result

# print(common_friends(["Аня", "Боря", "Витя"], ["Боря", "Галя", "Аня", "Витя"]))
    
    
    

    
# def most_active_day(dates):
#     counts = {}
    
#     for day in dates:
#         if day in counts:
#             counts[day] += 1
#         else:
#             counts[day] = 1
            
#     return counts
    
# print(most_active_day(["2025-05-01", "2025-05-01", "2025-05-02", "2025-05-02", "2025-05-02", "2025-05-03"])["2025-05-01"])




# def invert_dict(d):
     
#     inverted = {}
#     for key, value in d.items():
#         if value not in inverted:
#             inverted[value] = []
#         inverted[value].append(key)
#     return inverted
            
# print(invert_dict({"a": 1, "b": 2, "c": 1, "d": 3}))




# def longest_common_substring(s1, s2):
#     longest = ""
    
#     for i in range(len(s1)):
#         for j in range(i + 1, len(s1) + 1):
#             sub = s1[i:j]
#             if sub in s2 and len(sub) > len(longest):
#                 longest = sub
#     return longest
# print(longest_common_substring("acbetq", "qwracb"))


# def rle_encode(s):
#     result = ""
#     count = 1
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             result += f"{s[i - 1]}{count}"
#             count = 1
#     result += f"{s[-1]}{count}"

#     print(result) 
# rle_encode("AAABBCDDD") 
            
            
            
            
            
            
            
            
            
# def process(items):
#     result = []
#     for item in items:
#         if condition(item):
#             result.append(transform(item))
#     return result


# Вариации для переписывания:
# 1. Оставить только чётные числа

# def condition(item):
#     if item % 2 == 0:
#         return True
#     return False
# def transform(item):
#     return item
# print(process([1, 2, 3, 4, 5, 6]))

# 2. Оставить только строки длиной > 3

# def condition(item):
#     if len(item) > 3:
#         return True
#     return False
# def transform(item):
#     return item
# print(process(['qwe','ww','qwefsa']))

# 3. Удвоить все числа

# def condition(item):
#     if isinstance(item, (int, float)):
#         return True
#     return False
# def transform(item):
#     return item * 2
# print(process([1, 1.5, 'hello',]))
    
# 4. Перевести все строки в верхний регистр

# def condition(item):
#     if isinstance(item, str):
#         return True
#     return False
# def transform(item:str):
#     return item.upper()
# print(process([1, 1.5, 'hello', 'word']))

# 5. Оставить только положительные числа

# def condition(item):
#     if isinstance(item, (int, float)) > 0:
#         return False
# def transform(item):
#     return item


# 6. Извлечь из кортежей вторые элементы

# def condition(item):
#     if item is not None:
#         return True
#     return False
# def transform(item):
#     return item
    
    
           
# def process(items):
#     result = []
#     for first, second in items:
#         if condition(second):
#             result.append(transform(second))
#     return result

# print(process([(1,2), (5,7), ('a', 'b')]))

# 7. Оставить только уникальные

# def condition(item,res):
#     if item not in res:
#         return True
#     return False

# def transform(item):
#     return item

# def process(items):
#     result = []
#     for item in items:
#         if condition(item,result):
#             result.append(transform(item))
#     return result
# print(process([1, 1, 2, 3, 3, 124, 154, 154]))

# 8. Отфильтровать числа больше 10

# def condition(item):
#     if isinstance(item, (int, float)) and item > 10:
#         return False
# def transform(item):
#     return item


# 9. Преобразовать числа в строки

# def condition(item):
#     if isinstance(item, (int, float)):
#         return True
#     return False
# def transform(item):
#     return str(item)



# 10. Оставить только гласные буквы из строки

# def condition(item:str):
#     if item.isdigit() or item not in ['а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']:
#         return False
#     return True
# def transform(item):
#     return item
# print(process(""))