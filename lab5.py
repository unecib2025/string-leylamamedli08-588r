#1
name = input("Введите имя: ").strip()

if name.isalnum():
    name = name.lower()
    print("Имя корректно")
else:
    print("Ошибка")

#2
password = input("Введите пароль: ")

has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
is_long = len(password) >= 8

if has_digit and has_upper and is_long:
    print("Пароль надёжен")
else:
    print("Пароль ненадежен")

#3
log = "ACCESS DENIED"
format_log = log.capitalize() + " - вход запрещён"
print(format_log)

#4
data = "ERROR connection ERROR failed access"
modified_data = data.replace("ERROR", "ALERT")
alert_count = modified_data.count("ALERT")

print(f"Модифицированные данные: {modified_data}")
print(f"Количество предупреждений: {alert_count}")

#5
email = input("Введите email: ")

if email.find("@") != -1:
    parts = email.split("@")
    domain = parts[1] if len(parts) > 1 else ""
    print("Домен:", domain)
else:
    print("Некорректный адрес")

#6
text = input("Введите текст: ")
normal_text = text.strip().lower()
normal_text = normal_text.replace( "  ", " ")

print(f"Нормализованный текст: {normal_text}")

#7
text = input("Введите текст: ")
if text.find("SECRET") != -1:
    text = text.replace("SECRET", "******")
    print("Обнаружена конфиденциальная информация!")
    print(text)
else:
    print("Информация безопасна.")

#8
word = input("Введите слово: ")
# Преобразование в коды
codes = []
for char in word:
    codes.append(str(ord(char)))
print(f"Коды символов: {' '.join(codes)}")
# Обратное преобразование
reconstruct_word = ""
for code in codes:
    reconstruct_word += chr(int(code))
print(f"Восстановленное слово: {reconstruct_word}")

#9
text = "login attempt failed access denied unauthorized access"

failed_count = text.count("failed")
denied_count = text.count("denied")

print(f"Слово 'failed' встречается: {failed_count} раз")
print(f"Слово 'denied' встречается: {denied_count} раз")

if "failed" in text or "denied" in text:
    print("Попытка несанкционированного доступа")

#10
report = input("Введите отчёт: ")

# Количество предложений
sentences = report.split('.')
sentence_count = len([s for s in sentences if s.strip()])  # Игнорируем пустые строки

# Количество символов без пробелов
chars_without_spaces = len(report.replace(" ", ""))

# Проверка начала текста
starts_with_report = report.lower().startswith("report")

# Проверка на ошибки
error_count = report.lower().count("error")

print(f"Количество предложений: {sentence_count}")
print(f"Количество символов без пробелов: {chars_without_spaces}")
print(f"Начинается с 'Report': {'Да' if starts_with_report else 'Нет'}")
print(f"Количество упоминаний 'error': {error_count}")

if error_count >= 2:
    print("Ошибки найдены")




#1 Строка в Python - это неизменяемая последовательность символов Unicode
#2 Unicode - стандарт кодирования символов, который поддерживает все языки мира
#3 Методы строк:
   # strip() - удаляет пробелы по краям
   # replace() - заменяет подстроку
   # find() - ищет позицию подстроки
#4 Количество вхождений - метод count()
#5 Отличие:
   # upper() - все буквы в верхний регистр
   # capitalize() - только первую букву в верхний регистр
#6 ord() и chr():
   # ord() - возвращает код символа
   # chr() - возвращает символ по коду
#7 Проверка начала строки - метод startswith()
#8 Фильтрация данных важна для безопасности и предотвращения ошибок