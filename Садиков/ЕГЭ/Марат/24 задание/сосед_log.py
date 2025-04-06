import logging

# Настройка логирования
logging.basicConfig(filename='log.txt', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Открываем файл и считываем данные
f = open('сосед.txt')
s = f.read().rstrip()  # Удаляем пробелы и символы новой строки справа
f.close()  # Закрываем файл после чтения

# Инициализация переменных
k = 1
kmax = 0

logging.debug(f'Исходная строка: {s}')  # Логируем исходную строку

# Проходим по строке
for i in range(0, len(s) - 1):
    logging.debug(f'Итерация {i}: сравниваем {s[i]} и {s[i+1]}')  # Логируем текущую итерацию и сравниваемые символы
    if s[i] <= s[i + 1]:
        k = k + 1
        kmax = max(k, kmax)
        logging.debug(f'Условие выполнено: {s[i]} <= {s[i + 1]} | Текущий k: {k} | kmax: {kmax}')  # Логируем успешное выполнение условия
    else:
        k = 1
        logging.debug(f'Условие не выполнено: {s[i]} > {s[i + 1]} | Сбрасываем k на 1')  # Логируем сброс k

# Вывод максимальной длины последовательности
print(kmax)
logging.info(f'Максимальная длина последовательности: {kmax}')  # Логируем результат
