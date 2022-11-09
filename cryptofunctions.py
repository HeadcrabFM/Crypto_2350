# 2350 Соколов    |    +79217916237    |    M.L.Swgr@gmail.com
# Модуль для используемых функций

def slow_degree(number, degree, mod, lvl=2):
    """Быстрое возведение в степень по модулю"""
    low_degree = degree // lvl
    count = 1
    if degree % 2 == 0:
        min_lvl = 0
    else:
        min_lvl = 1
    for i in range(lvl - min_lvl):
        count *= number ** low_degree % mod
    return count * (number ** (degree - low_degree * (lvl - min_lvl)) % mod) % mod


def eul(n):
    """Считает функцию Эйлера"""
    import math
    q = 0
    for i in range(1, n):
        if (math.gcd(i, n) == 1):
            q += 1
        else:
            continue
    return q


def fermaeuler(a, m):
    """Теорема Ферма-Эйлера с исп. ф-и Эйлера
    Решает сравнение вида Ax=1(mod m)"""
    if mutprime(a, m):
        fi = eul(m)
        x = slow_degree(a, fi - 1, m, lvl=2)
        return x
    else:
        return False


def fermaeuler2(a, b, m):
    """Функция, решающая сравнение вида Ax=b(mod m) с использованием теор. Ферма-Эйлера
    Решает сравнение вида Ax=B(mod m)"""
    x = slow_degree((fermaeuler(a, m) * b), 1, m)
    return x


# Проверка на простое надо добавить Алгоритм миллера = ?
def issimple(a):
    """Проверка на простоту перебором"""
    for i in range(2, (a // 2) + 1):
        if (a % i == 0):  # если остаток от деления на какое-то число = 0
            return False  # -> число не простое
    return True


def mutprime(a, b):
    """Проверка на взаимную простоту"""
    import math
    if math.gcd(a, b) == 1:
        return True
    else:
        return False


def inbetween(x, a, b):
    """Простая проверка на нахождение в промежутке"""
    if x <= a or x >= b:
        return False
    else:
        return True


# * * * ИНТЕРФЕЙСНЫЕ ФУНКЦИИ ВВОДА/ВЫВОДА * * *


def inputprimecheck(message=str, message_fail=str):
    """функция ввода с клавиатуры с проверкой на простое"""
    x = int(input(message))
    while (issimple(x) != True):
        x = int(input(message_fail))
    return x


def inputmutprimecheck(y, message=str, message_fail=str):
    """функция ввода с клавиатуры с проверкой на взаимную простоту"""
    x = int(input(message))
    while (mutprime(x, eul(y)) != True):
        x = int(input(message_fail))
    return x


# 20.10
def input_inbetween_check(a, b, message=str, message_fail=str):
    """Проверка нахождения вводимого числа в промежутке"""
    x = int(input(message))
    while inbetween(x, a, b) == False:
        x = int(input(message_fail))
    return x


def input_mutprime_inbetween(a, b, c, message=str, message_fail=str):
    """Проверка на нахождение в промежутке
     + на взаимную простоту с заданным числом"""
    x = int(input(message))
    while mutprime(x, c) == False or inbetween(x, a, b) == False:
        x = int(input(message_fail))
    return x


def message_input(a, prompt=str, message_fail=str):
    """Ввод сообщения с проверкой длины"""
    m = int(input(prompt))
    while m >= a:
        m = int(input(message_fail))
    return m


# три функции для преобразования строку сообщения в список цифр (коды символов)
# коды символов удобно передавать через протоколы отдельно и получать не просто цифры а текст
# ASCII имеет 127 символов (англ раскладка)

def text_crypt(message):
    """Функция для разбиение введённой строки
    на символы и сохранение кода каждого символа в список.
    Возвращает список с кодами сомволов ввенной строки
    Удобно для последовательной передачи каждого кода по протоколу"""
    crypt_messg = []
    for i in range(len(message)):
        crypt_messg.append(ord(message[i]))
    return crypt_messg


def text_decrypt(crypt_messg):
    """Функция преобразующая список кодов символов обратно в текст
    Возвращает строку с символами"""
    decrypt_messg = []
    for i in range(len(crypt_messg)):
        decrypt_messg.append(chr(crypt_messg[i]))
    return decrypt_messg


def text_output(decrypt_messg, info=str):
    """Функция вывода списка в виде строки (текста) в консоль"""
    print(info, end=' ')
    print("".join((map(str, decrypt_messg))))


def text_equalcheck(message=list, message2=list):
    """Функция проверки совпадения отправленного и расшифр. сообщ."""
    for i in range(len(message)):
        if message[i] != message2[i]:
            return False
    return True


def text_equalcheck2(message=list, message2=list):
    """Функция проверки совпадения отправленного и расшифр. сообщ."""
    if message == message2:
        return True
    return False
