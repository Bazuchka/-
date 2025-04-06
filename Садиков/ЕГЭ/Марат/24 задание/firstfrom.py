import re  # Импортируем модуль re для работы с регулярными выражениями
import logging  # Импортируем модуль logging для ведения журнала событий

# Настройка логирования
logging.basicConfig(
    filename='app.log',  # Указываем имя файла для сохранения логов
    level=logging.DEBUG,  # Устанавливаем уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат сообщений
)

# Читаем первую строку из файла 'demo_2025_24.txt', убираем пробелы в начале и конце
logging.debug('Opening the file demo_2025_24.txt to read the first line.')
try:
    s = open('demo_2025_24.txt').readline().strip()
    logging.debug(f'Read line: "{s}"')
except FileNotFoundError:
    logging.error('The file demo_2025_24.txt was not found.')
    raise

# Используем регулярное выражение для поиска всех подстрок, которые соответствуют заданному шаблону
logging.debug('Searching for patterns in the string using regex.')
pattern = r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))*'
expr = re.findall(pattern, s)

# Логируем количество найденных совпадений
logging.debug(f'Found {len(expr)} matches: {expr}')

# Создаем новый список, в котором сохраняем длины каждой найденной подстроки
expr_len = []
for index, match in enumerate(expr):
    length = len(match)
    expr_len.append(length)
    logging.debug(f'Iteration {index + 1}: Found match "{match}" with length {length}.')

# Логируем длины найденных совпадений
logging.debug(f'Lengths of found matches: {expr_len}')

# Печатаем максимальную длину среди всех найденных подстрок
if expr_len:  # Проверяем, что список не пустой
    max_length = max(expr_len)
    logging.debug(f'Maximum length of matches: {max_length}')
    print(max_length)
else:
    logging.warning('No matches found, cannot determine maximum length.')
