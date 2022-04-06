print ('my first python file')
# выполняю пример с паролем
original_password = "delta12345"
password = input('Введите пароль с учетом регистра: ')
access = False #переменная, хранит разрешение на доступ - разобраться!
if password == original_password:
    print ('Четовски верный пароль!')
    access = True
if password != original_password:
    print ('думай дальше - ты ввел неверный пароль')

