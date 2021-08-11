import os

# Start code

print(os.getcwd())  # Получаем текущию директорию
road_to = input()  # Получаем от пользователя путь для смены директории
save_road_to = (os.chdir(road_to))  # Храним в переменной путь для смены директории
print(os.listdir(save_road_to))  # Выводим список файлов в директории

print("1 чтобы создать директорию \n 2 если нехотите создавать директорию \n 3 для удаления(если директория пустая)")
answer = int(input())

if answer == 1:
    print("Введите название директории:")
    name_for_directory = str(input())
    os.mkdir(name_for_directory)
elif answer == 2:
    print("Завершение работы.")
    exit()
else:
    print('Введите название директории: ')
    name_for_delete_directory = str(input())
    os.rmdir(name_for_delete_directory)
    print(os.listdir(save_road_to))
