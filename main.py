import os
import time

# Start code

print(f'Вы находитесь в этой директории: {os.getcwd()}')
print('Хотите перейти в другую директорию?')
first_answer = str(input())
if first_answer == 'Да':
    print('Введите путь: ')
    road_directory = str(input())
    print('Переходим в директорию...')
    time.sleep(1)
    print('Готово. Получаем содержимое директории')
    time.sleep(1)
    print(os.listdir(road_directory))
    print('Что вы хотите сделать дальше?')
    time.sleep(1)
    print('Создать Директорию? Удалить?')
    second_answer = str(input())
    if second_answer == 'Создать':
        print('Название директории: ')
        four_answer =str(input())
        os.mkdir(four_answer)
        print('Создаём...')
        print('Готово!')
        time.sleep(1)
        print(os.listdir(road_directory))
    else:
        print(os.getcwd())
        print('Введите полный путь для удаления')
        delete_answer = str(input())
        os.removedirs(delete_answer)