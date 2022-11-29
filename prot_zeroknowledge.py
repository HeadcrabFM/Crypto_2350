import cryptofunctions as crf
import math
import random


# Протокол с нулевой передачей данных оформлен в одну длинную функцию без разбиения

def zero_knowledge():
    openkey = []  # список открытых ключей
    openkey_reverse = []  # обратные к откытым ключам
    secretkey = []  # список секретных ключей s
    mutprime_n = []  # список кв.вычетов n, взаимно простых с n
    vychety = []  # список кв.вычетов n
    ping = [0, 1]  # Список возможных сигналов отправляемыз на втором шаге

    p = crf.inputprimecheck('Введите простое р: ', 'НЕ ЯВЛЯЕТСЯ простым, введите ПРОСТОЕ р: ')
    q = crf.inputprimecheck('Введите простое q: ', 'НЕ ЯВЛЯЕТСЯ простым, введите ПРОСТОЕ q: ')
    n = p * q
    print(f'Полученный модуль n = p*q = {n}')
    print(f'\nВсе квадратичные вычеты для {n}: (проверяем до половины n)')

    # заполняем список кв.вычетов n, взаимно простых с n
    for i in range(1, n // 2 + 2):
        d = pow(i, 2, n)
        vychety.append(d)
        print(f'для {i}: {d}, gcd: {math.gcd(i, n)}')
        if math.gcd(d, n) == 1:
            mutprime_n.append(d)
    # удаляем из списка взаимно простых с n вычетов повторяющиеся:
    mutprime_n = list(set(mutprime_n))

    # выбираем количество vi
    try:
        kol = int(input('\nВведите q - желаемое количество vi (1<q<5): '))
    except:
        raise ValueError('НЕТ! ЛОх')

    # выбираем открытые ключи vi взаимно простые с n
    print(
        f'Из приведённого ниже списка вычетов необходимо выбрать {kol} вычета (открытых ключа vi) таких, что (a,n)=1:\n{mutprime_n}\n')
    for i in range(kol):
        v = crf.inputmutprimecheck2(n,
                                    f'Введите открытый ключ v{i + 1} из списка кв.вычетов для {n}, взаимно простых с {n}: ',
                                    f'Не взамно просты. Введите v{i} взаимно простое с {n}: ')
        openkey.append(v)
    print(f'\nВыбранные открытые ключи: {openkey}')

    # ищем обратные ключи и заполняем список
    for i in range(kol):
        openkey_reverse.append(crf.fermaeuler(openkey[i], n))
    print(f'Найденные обратные vi: {openkey_reverse}')

    # ищем секретные ключи S
    for i in range(kol):
        for j in range(len(vychety)):
            if openkey_reverse[i] == vychety[j]:
                secretkey.append(j + 1)
                break
        else:
            print('какаято ошибка. НЕ получилось определить S')

    # выводим на экран введённые и полученные данные
    print(f'Найденные секретные ключи Si: {secretkey}\n')
    print(f'>>> Начало передачи')
    r = int(input('Введите любое случайное положительное r < n (по нему будет проив. проверка):\n'))

    b_list = []  # список для хранения сигналов b = 0 v 1, передаваемых на шаге 2

    # шаг 1
    message = pow(r, 2, n)
    print(f'Шаг 1:   A -> B  {message}')

    # шаг 2
    for i in range(kol):
        b = random.choice(ping)
        b_list.append(b)
    print(f'Шаг 2:   B -> A  {b_list}')

    # шаг 3
    y = int(r)
    for i in range(kol):
        y *= secretkey[i] ** b_list[i]
    y = pow(y, 1, n)
    print(f'Шаг 3:   A -> B  {y}')

    # шаг 4
    d = y ** 2
    for i in range(kol):
        d *= openkey[i] ** b_list[i]
    d = pow(d, 1, n)
    print(f'Шаг 4:   B:  {d}')

    if crf.text_equalcheck2(message, d):
        print('Результаты шага 1 и 4 сошлись -> аутентификация пройдена успешно')
        return True
    else:
        print('Результаты шага 1 и 4 НЕ сошлись -> аутентификация НЕ пройдена!')
        return False


a = 0
i = 1
check = []
print(' * * * ПРОТОКОЛ С НУЛЕВОЙ ПЕРЕДАЧЕЙ ЗНАНИЙ * * *')

while a == 0:  # Цикл для зацикливания тестирования
    print(f'\n>>> ТЕСТ №{i}')

    x = zero_knowledge()  # получаем функцию, которую можно вызвать в 1 строчку без передачи аргументов на вход

    if x:
        check.append(f'Тест {i}: успех')
    else:
        check.append(f'Тест {i}: неудача')
    a = int(input('\nНажмите 0 для продолжения тестирования, любую другую цифру для выхода: '))
    i += 1

print(f'ИТОГИ ТЕСТИРОВАНИЯ:\n{check}')
input('\nКОНЕЦ ТЕСТИРОВАНИЯ\n\n* * * Press Enter to exit... * * *')
