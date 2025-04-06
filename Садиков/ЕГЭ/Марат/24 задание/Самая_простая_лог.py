import logging  # Импортируем модуль logging для ведения журнала событий

# Настройка логирования
logging.basicConfig(
    filename='app.log',  # Указываем имя файла для сохранения логов
    level=logging.DEBUG,  # Устанавливаем уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат сообщений
)

# Открываем файл '24_1.txt' и читаем его содержимое
try:
    with open('24_1.txt', 'r') as f:
        s = f.read()
        logging.debug(f'Read content from file: "{s}"')
except FileNotFoundError:
    logging.error('The file 24_1.txt was not found.')
    raise

k = 0  # Переменная для подсчета текущих подряд идущих 'B'
kmax = 0  # Переменная для хранения максимального количества подряд идущих 'B'

# Проходим по каждому символу в строке
for index in range(len(s)):
    logging.debug(f'Iteration {index + 1}: Current character: "{s[index]}"')
    
    if s[index] == 'B':
        k += 1  # Увеличиваем счётчик, если символ 'B'
        logging.debug(f'Character is B. Incrementing count: k = {k}')
        
        # Обновляем максимальное количество подряд идущих 'B'
        kmax = max(k, kmax)
        logging.debug(f'Updated maximum count: kmax = {kmax}')
    else:
        logging.debug(f'Character is not B. Resetting count.')
        k = 0  # Сбрасываем счётчик, если символ не 'B'

# Печатаем максимальное количество подряд идущих 'B'
logging.info(f'Maximum number of consecutive B: {kmax}')
print(kmax)
