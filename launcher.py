import os

"""Файл создан для возможности запускать главное меню
(cryptofunctions.launcher) чтобы избежать циклического импорта"""
import prot_nokey as lr1
import prot_RSA as lr2
import prot_elgamal as lr3
import chinesetheorem as lr4
import prot_zeroknowledge as lr5
import hashfunction as lr6


def mainlauncher():
    """Функция для возможности запуска
    лабораторных из главного меню
    и возврата в него по окончании тестирования.
    т.к. все лабораторные запускаются """
    name = ['1  -  протокол без передачи ключа',
            '2  -  протокол с открытым ключом',
            '3  -  система Эль Гамаля',
            '4  -  китайская теорема об остатках',
            '5  -  потокол с нулевой передачей знаний',
            '6  -  хэш-функция',
            '0  -  выход']

    print("\n\n* * * ГЛАВНОЕ МЕНЮ * * *\nВведите номер ЛР для тестирования: ")
    for i in range (len(name)):
        print(name[i])

    a = int(input("\n>>>  "))
    if (a == 0):
        print("Работа программы завершена. Press any key to exit .  .   .    .")
        # Прощание, кредиты (функция cryptofunctions.credits)
        input()
        exit()
    if (a == 1):
        os.system('cls')  # очистка консоли
        lr1.launch()
    if (a == 2):
        os.system('cls')  # очистка консоли
        lr2.launch()
    if (a == 3):
        os.system('cls')  # очистка консоли
        lr3.launch()
    if (a == 4):
        os.system('cls')  # очистка консоли
        lr4.launch()
    if (a == 5):
        os.system('cls')  # очистка консоли
        lr5.launch()
    if (a == 6):
        os.system('cls')  # очистка консоли
        lr6.launch()
