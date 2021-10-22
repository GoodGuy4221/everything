f_name = 'file.txt'

try:
    file = open(f_name, 'r', encoding='utf-8')
except FileNotFoundError as e:
    print(f'файла не существует: {e}')
except FileExistsError as e:
    print(f'файл существует {e}')
except Exception as e:
    print(f'неизвестная ошибка {e}')
else:
    for line in file:
        print(line.strip())
    file.close()
