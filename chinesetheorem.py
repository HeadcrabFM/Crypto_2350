from cryptofunctions import *

"""Китайская теорема об остатках (КТО)"""


def cht_input():
    """КТО :: функция ввода данных"""
    system = []
    q = int(input('\nНеобходимо ввести ряд сообщений вида x = a (mod m)\nВведите количество уравнений в системе: '))
    a = []
    m = []
    for i in range(q):
        # Нужна проверка на простоту всего введнного
        a.append(int(input(f'\n>>> Ввод уравнения системы №{i + 1} из {q}\nВведите a{i + 1}: ')))
        m.append(
            int(input_mutprime_full(m, f'Введите m{i + 1}: ', f'Не взаимно с каким-то из ранее введнных m, ещё раз: ')))
    system.append(a)
    system.append(m)

    # Вывод введенной системы на экран
    print(f'\nВведённая система:')
    for i in range(len(system[0])):
        print(f'x = {system[0][i]} (mod {system[1][i]})')

    return system


def cht_process(system):
    """КТО :: функция обработки данных"""
    # Определяем М = П(0,i)mi
    M = 1
    for i in range(len(system[0])):
        M *= system[1][i]
    print(f'\nНайденное произведение ряда М: {M}\n')

    # определяем каждую Mi = M/mi
    Mi_list = []
    for i in range(len(system[0])):
        Mi_list.append(M // system[1][i])
        print(f'M{i} = {Mi_list[i]}')  # вывод полученных Mi
    print('')

    # Находим все Ni, решая сравнения: Mi*Ni=1(mod mi) с помощью ферма эйлера fermaeuler
    Ni_list = []
    for i in range(len(system[0])):
        Ni_list.append(fermaeuler(Mi_list[i], system[1][i]))
        print(f'N{i} = {Ni_list[i]}')  # вывод полученных Ni

    # Находим х = ROWSUM (ai*Ni*Mi(mod M))
    x = 0
    for i in range(len(system[0])):
        x += system[0][i] * Ni_list[i] * Mi_list[i]
    x = slow_degree(x, 1, M, lvl=2)

    # Эти три строчки просто для вывода формулы, моно удалить
    print(f'\nФормула рассчёта итогового x: x = {system[0][0] * Ni_list[0] * Mi_list[0]}', end='')
    for i in range(1, len(system[0])):
        print(f' + {system[0][i]}*{Ni_list[i]}*{Mi_list[i]}', end='')
    print(f' (mod {M})')

    print(f'\nИтоговый х: {x}')


def cht():
    """КТО: общая функция обработки"""
    system = cht_input()
    cht_process(system)

def launch():
    a = 0
    i = 1
    while a == 0:  # Цикл для зацикливания тестирования
        print(' * * * КИТАЙСКАЯ ТЕОРЕМА ОБ ОСТАТКАХ * * *')
        print(f'\n>>> ТЕСТ №{i}')
        cht()  # получаем функцию, которую можно вызвать в 1 строчку без передачи аргументов на вход
        a = int(input('\nНажмите 0 для продолжения тестирования, любую другую цифру для выхода: '))
        i += 1
    input('\nКОНЕЦ ТЕСТИРОВАНИЯ\n\n* * * Press Enter to exit... * * *')
    mainmenu()