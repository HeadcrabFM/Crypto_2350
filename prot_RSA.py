import cryptofunctions

def rsa_input(x, y, abonent, a):
    print(f'\nВвод данных для абонента {abonent}')
    p1 = cryptofunctions.inputprimecheck(f'Выберите простое число {x} для {abonent}: ', 'Выберите ПРОСТОЕ число: ')
    p2 = cryptofunctions.inputprimecheck(f'Выберите простое число {y} для {abonent}: ', 'Выберите ПРОСТОЕ число: ')
    r = p1 * p2
    openkey = cryptofunctions.inputmutprimecheck(r,
                                           f'Введите открытый ключ {a}, меньший {cryptofunctions.eul(r)} и взаимно простый с ним: ',
                                           f'Неудача. Введите а, которое МЕНЬШЕ и взаимно просто с {cryptofunctions.eul(r)}: ')
    secretkey = cryptofunctions.fermaeuler(openkey, cryptofunctions.eul(r))
    l=[p1,p2,r,openkey,secretkey]
    print(f'Данные для абонента {abonent}: {l}')
    return l

def message_input(r,a,b):
    print(f' * * * ПЕРЕДАЧА СООБЩЕНИЯ ОТ АБОНЕНТА {a} АБОНЕНТУ {b} * * *\n')
    m = m1 = int(input('Введите  сообщение m: '))
    while m >= r:
        m = m1 = int(input(f'm должно быть меньше {cryptofunctions.eul(r)}. Введите m: '))
    return m,m1

def rsa_process(message, r, openkey, secretkey):    # Непосредственно сама обработка
    message=cryptofunctions.slow_degree(message,openkey,r,lvl=2)
    print(f'\n1.   A -> B:  {message}')
    message=cryptofunctions.slow_degree(message,secretkey,r,lvl=2)
    print(f'2.   B:   {message}')
    return message

def rsa_check(m,m1):
    if m1==m:
        check=True
        print('\nРасшифрованное сообщение сходится с исходным')
    else:
        print('\nРасшифрованное сообщение НЕ сходится с исходным')
        check=False
    return check

def RSA(): # Rivest Shamir Adelman
    print(' * * * ПРОТОКОЛ ШИФРОВАНИЯ С ОТКРЫТЫМ КЛЮЧОМ 2 * * *')
    l1=rsa_input('p1', 'p2', 'A', 'a')
    l2=rsa_input('q1', 'q2', 'B', 'b')
    print(f"\nСекретные ключи:\nАльфа = {l1[4]}\nБета = {l2[4]}")

    m,m1=message_input(l2[2],'A','B')
    rsa_process(m1, l2[2], l2[3], l2[4])
    rsa_check(m,m1)
    input('Print any key to exit . . .')
    cryptofunctions.mainmenu()

def launch():
    RSA() # вызов функции одной строкой