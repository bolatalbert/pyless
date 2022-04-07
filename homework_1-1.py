# Альберт, задание 1
name = input("Введите Ваше имя: ")
age = int(input("Сколько Вам лет: "))
country = input("Из какой Вы страны: ")
pet = input("Имя домашнего животного: ")
print(f"Вас зовут: {name} , Вам {age} лет, Вы из {country} и у Вас есть животное по имени {pet}")

# задание 2 -- про часы

time = int(input("Введите время в секундах (введите целое число): "))
if time <= 59:
    print (f"00:00:{time}")
if time >= 60:
    print (f"00:{time // 60}:{(time - (time // 60) * 60)}")
if time >= 3600:
    print (f"{time // 3600}:{(time - 3600) // 60}:{(time - (time // 60) * 60)}")
else:
    print('неверный формат ввода')

