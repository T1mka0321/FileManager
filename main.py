import os
import time

'''
Автор кода: T1murka0321 
Ps: Только учусь кодить в питоне
'''

# Start code

print(f'Вы находитесь в этой директории: {os.getcwd()}')    # Показываем текущую директорию
print('Хотите перейти в другую директорию?')    # Это и так понятно
first_answer = str(input() )    # Записываем ответ
if first_answer == 'Да':  # Делаем проверку ответа если Да то код продолжается
    print('Введите путь: ')  # Вводим путь директории 
    road_directory = str(input())  # Записывем путь директории
    print('Переходим в директорию...')  # Это и так понятно
    time.sleep(1)  # Для эстетики
    print('Готово. Получаем содержимое директории')  # Это и так понятно
    time.sleep(1)  # Для эстетики
    print(os.listdir(road_directory))  # os.listdir получает содержимое директории
    print('Что вы хотите сделать дальше?')  # Это и так понятно
    time.sleep(1)  # Для эстетики
    print('Создать Директорию? Удалить?')  # Это и так понятно
    second_answer = str(input())
    if second_answer == 'Создать':
        print('Название директории: ')
        four_answer =str(input())
        os.mkdir(four_answer)
        print('Создаём...')
        print('Готово!')
        time.sleep(1)
        print(os.listdir(road_directory))

# Пока что всё
print('Good bye!')