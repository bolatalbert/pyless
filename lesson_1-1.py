# print ('my first python file')
# выполняю пример с паролем
# original_password = "delta12345"
# password = input('Введите пароль с учетом регистра: ')
# access = False #переменная, хранит разрешение на доступ - разобраться!
# if password == original_password:
# print ('Четовски верный пароль!')
# access = True
# if password != original_password:
# print ('думай дальше - ты ввел неверный пароль')
# все переменные в нижнем регистре!
# if age >= 18 and country == "Russia" # оба age и country должны быть True!!
# если там or -- то хотя бы одно должно быть True

# name = input ("Enter your name: ")
# print ("Hi, ", name, "!")

# Ветвления
# or_pass = "12345"
# passowrd2 = input("Enter your password: ")

# if passowrd2 == or_pass:
# print("OK!")

# if passowrd2 !== or_pass:
# print("error!")
# интерпретатор пройдет по ВСЕМ if !!!

# if passowrd2 == or_pass: # если выражение верно == истинно
# print ('OK!')
# else: # else не имеет своего логического выражения -- он живет в if -- выражение после if неверно
# print ("error")

# elif --

# color = input ("Enter you color: ")

# if color == "black":
#  print (121)
# elif color == "blue":
#   print (222)
# elif color == "green":
#  print (333)
# elif color == "red":
#  print (2222)
# else:
# print ("У меня не хватило ума определить цвет")

# циклы while -- цикл продолжается пока выражение истинно. как только оно станет false - все

# num = int(input("Enter a number 0-9: "))

# while num <= 10:
#    print(num)
#    num = num + 1 # краткая запись: num += 1

# операторы управления циклом

num = 0

while True:  # бесконечный цикл
    num += 1
    if num >= 10:
        break
    if num % 2 == 0:
        continue
    print(num)

f"{100 / 17:.6f}

