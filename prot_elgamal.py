import cryptofunctions as crf

def elgamal_input(abonent):
    """Эльгамаль :: Функция для ввода данных с клавиатуры"""
    p = crf.inputprimecheck(f'Введите простое р: ', f'Это не простое. Введите ПРОСТОЕ р: ')
    g = crf.input_inbetween_check(1, p, f'Введите любое G такое, что 1 < G < {p}: ',
                                  f'Не подходит. Введите любое G такое, что 1 < G < {p}: ')
    x = crf.input_inbetween_check(1, p, f'Выберите секретный ключ х (1 < х < {p}): ',
                                  f'Выберите другой секретный ключ 1 < х < {p}: ')
    k = crf.input_mutprime_inbetween(1, p - 1, p - 1,
                                     f'Выберите такое целое k, что:\n1 < k < {p - 1} и взаимно простое с {p - 1}: ',
                                     f'Не подходит, выберите 1 < k < {p - 1} и взаимно простое с {p - 1}: ')

    abonent_info = [abonent, p, g, x, k]
    print(f'\nДанные для абонента: {abonent_info}')
    return abonent_info


def elgamal_process(ab_info, letter, no):
    """Эльгамаль :: Функция обрабатывающая введённые данные"""
    openkey = pow(ab_info[2], ab_info[3], ab_info[1])
    a = pow(ab_info[2], ab_info[4], ab_info[1])
    b = crf.slow_degree((openkey ** ab_info[4]) * letter, 1, ab_info[1])

    print(f'\nОткрытый ключ:    {openkey}\nЧисло а:    {a}\nЧисло b:    {b}\n')
    print(f'На шаге {no} адресат получает от абонента {ab_info[0]} пару чисел: a = {a}, b = {b}\n')
    res = crf.fermaeuler2(a ** ab_info[3], b, ab_info[1])
    print(f'После расшифровки, абонент получает код символа №{no}: {res} -> символ "{chr(res)}"\n')
    return res


def elgamal():
    """Эльгамаль :: функция полного протокола"""
    print(' * * * ПРОТОКОЛ ШИФРОВАНИЯ ЭЛЬ ГАМАЛЯ * * *\n')
    ab1 = elgamal_input(input(f'Введите имя абонента: '))

    text = crf.text_crypt(input("Введите текст сообщения на английском: "))
    text2 = []
    print(f'\nДлина сообщения: {len(text)}')
    for i in range(len(text)):
        print(f'>>> Шаг {i + 1}. Обработка символа №{i + 1}: <<{chr(text[i])}>>')
        res = elgamal_process(ab1, text[i], i + 1)
        text2.append(res)
    crf.text_output(crf.text_decrypt(text2), '\nРасшифрованное сообщение: ')  # вывод на экран


    #поправить проверку совпадения сообщений. можно проще сделать.
    if crf.text_equalcheck2(text, text2):
        print("Отправленное и расшифрованное сообщения сошлись")
    else:
        print("Отправленное и расшифрованное сообщения НЕ сошлись")


a = 0
i = 1
while a == 0:  # Цикл для зацикливания тестирования
    print(f'\n>>> ТЕСТ №{i}')
    elgamal()  # получаем функцию, которую можно вызвать в 1 строчку без передачи аргументов на вход
    a = int(input('\nНажмите 0 для продолжения тестирования, любую другую цифру для выхода: '))
    i += 1
input('\nКОНЕЦ ТЕСТИРОВАНИЯ\n\n* * * Press Enter to exit... * * *')
