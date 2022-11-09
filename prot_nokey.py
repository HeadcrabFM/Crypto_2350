import cryptofunctions


# Функция протокола шифрования без передачи ключа
def prot_nokey():
    print(' * * * ПРОТОКОЛ ШИФРОВАНИЯ БЕЗ ПЕРЕДАЧИ КЛЮЧА * * *\n')
    # БЛОК ВВОДА ДАННЫХ
    # Выбор простого числа и откытых ключей
    p = cryptofunctions.inputprimecheck('Выберите трёхзначное простое число р: ', 'Выберите ПРОСТОЕ р: ')
    a = cryptofunctions.inputmutprimecheck(p, 'Выберите открытый ключ а :',
                                           f'Выберите a, взаимно простое к {cryptofunctions.eul(p)} :')
    b = cryptofunctions.inputmutprimecheck(p, 'Выберите открытый ключ b :',
                                           f'Выберите b, взаимно простое к {cryptofunctions.eul(p)} :')

    # Ввод сообщения с проверкой длины
    m = m1 = int(input('Введите  сообщение m: '))
    while m >= p:
        m = m1 = int(input('m должно быть меньше p. Введите m: '))

    # БЛОК ОБРАБОТКИ
    # непосредственно обработка сообщения
    alpha = cryptofunctions.fermaeuler(a, cryptofunctions.eul(p))  # функция эйлера от простого р = (р-1)
    beta = cryptofunctions.fermaeuler(b, cryptofunctions.eul(p))
    print(f"\nСекретные ключи:\nАльфа = {alpha}\nБета = {beta}")
    res = cryptofunctions.slow_degree(m1, a, p, lvl=2)
    print("\n1.   A -> B: ", res)
    res = cryptofunctions.slow_degree(res, b, p, lvl=2)
    print("2.   B -> A: ", res)
    res = cryptofunctions.slow_degree(res, alpha, p, lvl=2)
    print("3.   A -> B: ", res)
    res = cryptofunctions.slow_degree(res, beta, p, lvl=2)
    print(f'4.        B:  {res}')
    return res


prot_nokey()  # в итоге получаем функцию протокола с возможностью ввода данных кот. можно вызвать одной строкой
input('\n\n * * * Press any key to exit... * * *')
