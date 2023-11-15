# Если скрипт запущен не от имени администратора, тогда он не будет норально работать (не сможет взламывать, но сможет генерировать словарь)
#  чтобы скрипт сам проверял, запущена ли оболочка командной строки от имени администратора или нет, и если нет, перезапускал бы скрипт, но уже в оболочке, запущенной с правами администратора?
import ctypes
import sys

import psutil #если не установлен модуль psutil, его надо установить с помощью команды: pip install psutil


def printing():
    print('Скрипт запущен с правами администратора. Нажмите кнопку Enter')
    for app in psutil.process_iter(['pid', 'name']):
        sys_app = app.info.get('name').split('.')[0].lower()
        if 'powershell' in sys_app or 'cmd' in sys_app:
            try:
                psutil.Process(app.info.get('pid')).terminate()
                break
            except:
                continue
    input()


def main():
    printing()


if ctypes.windll.shell32.IsUserAnAdmin():
    if __name__ == "__main__":
        main()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

# ДАЛЬШЕ ИДЕТ ОСНОВНОЙ КОД

import zipfile  # для работы с файлами zip
import py7zr
# секундомер. Необходимо установить (pip install stopwatch.py)
from stopwatch import Stopwatch
import time  # для создания эффекта печатания текста с задержкой
    # для работы с файлами rar необходмио установить (pip install unrar)
from unrar import rarfile
    # секундомер. Необходимо установить (pip install stopwatch.py)
import msoffcrypto  # для работы с офисными файлами
import io  # для работы с файлами с расширениями docx и xlsx
    # для созлания разноцветного текста в программе. Необходимо установить (pip install colorama)
from colorama import init, Fore, Style
init()

print(Style.BRIGHT + Fore.RED)
print("Если не работает, необходмо установить необходимые библиотеки. Нажмите цифру 5 для автоматической установки")
# print("pip install psutil - для запуска с правами администратора")
# print("pip install unrar - для работы с rar архивами") 
# print("pip install msoffcrypto-tool - для работы с документами office")
# print("pip install py7zr - для работы с архивами 7z")
# print("pip install stopwatch.py - для отображения секундомера")
# print("pip install colorama - для создания разноцветного текста")

def startProgramm():
    print(Style.BRIGHT + Fore.GREEN)    # для созлания разноцветного текста в программе. Необходимо установить (pip install colorama)
    print("Программа для взлома запороленных архивов и документов MS Office, а также создание словарей")
    print('1. Взлом архивов RAR и ZIP ')
    print('2. Взлом архива 7z')
    print('3. Взлом документов MS Office')
    print('4. Создание словаря')
    print('5. Загрузить модули')

    choose = input ('Выберите то, что хотите сделать. Нажмите соответсвующую цифру на клавиатуре:  ')

    def importRar():


        def console_picture():
            print(Style.BRIGHT + Fore.CYAN)
            print("   ########   ########  ##      ##   #######   ########    ######## ")
            print("   ########   ########  ##      ##   ##    ##  ##          ######## ")
            print("   ##    ##   ##    ##  ##     ###   ########  ########       ##  ")
            print("   ##    ##   ########  ##  ##  ##   ##    ##  ##             ##  ")
            print("   ##    ##   ##        ## #    ##   ########  ########       ##  ")
            print("   ##    ##   ##        ##      ##   #######   ########       ##  ")
            print()
            print()
            print("   ########      ###    ##      ##   ########   ##      ##  ########     @@ ")
            print("   ##           #####   ##      ##   ##    ##   ##      ##  ########     @@ ")
            print("   ######      ##   ##  ##########   ##    ##   ##      ##     ##        @@ ")
            print("   ##    ##   ##     ## ##      ##   ##    ##   ##    ####     ##        @@ ")
            print("   ########   ######### ##      ##   ##    ##   ##  ##  ##     ##        @@ ")
            print("   ######     ##     ## ##      ##  ##########  ## #    ##     ##           ")
            print("                                    ##      ##  ##      ##     ##        @@ ")
            print()
            print()
            print()


        console_picture()


        wordTitle = '          Программа для взлома запароленных zip и rar архивов '
        # создаем эффект печатания текста (текст выводиться с задержкой)
        for i in wordTitle:
            print(i.upper(), end="")
            time.sleep(0.03)

        stopwatch = Stopwatch(2)  # 2 это десятична точность для секундомера


        def crack_password(password_list, file_for_breaking):

            indx = 0
            cnt = len(list(open(password_list, 'rb')))
            # открываем файл (with open() as file: - пишем так, чтобы потом не писать комманду закрытия файла (close()). rb открытие в двоичном режиме )
            with open(password_list, 'rb') as file:
                stopwatch.restart()
                for line in file:
                    for word in line.split():
                        # вычисляем в процентном соотношении количество пребранных паролей
                        x = (indx+1)/cnt * 100
                        # отсекаем цифры после запятой до 2-х, чтоб не получалось вроде такого: 0.9834539503%
                        x = float('{:.2f}'.format(x))
                        print(
                            f'Количество перебранных паролей {indx} ----- Процент перебранных паролей {x} ---- Прошло времени {str(stopwatch)}\r', end="")  # подсчитываем количество перебранных паролей. Вывод текста в одну строку с затиранием предыдущего
                        try:
                            indx += 1
                            # # pwd: если zip-файл зашифрован, передайте пароль в этом аргументе (по умолчанию: None) .
                            # делаем проверку, имеется ли в имени файла расширения файла zip или rar
                            if (file_for_breaking.filename.endswith('.zip')):
                                file_for_breaking.extractall(pwd=word)
                            elif (file_for_breaking.filename.endswith('.rar')):
                                file_for_breaking.extractall(pwd=word.decode("utf8"))
                            print("\n")
                            print(Style.BRIGHT + Fore.GREEN)
                            print("Пароль найден в строке: ", indx)
                            # Декодирует байтстроку в строку.
                            print("Пароль: ", word.decode())
                            stopwatch.reset()  # сбрасываем счетчик на 0
                            # После нахождения пароля, спрашиваем про желание продолжить взламывать пароли
                            print(Style.BRIGHT + Fore.YELLOW)
                            continue_work = input(
                                "Хотите продолжить? Если да, то нажмите букву 'д', если хотите выйти в главное меню нажмите - 0:_")
                            if (continue_work == 'д'):
                                main_data()
                                # return True
                            elif (continue_work == '0'):                                
                                startProgramm()
                            else:
                                return True

                        except:

                            continue
            return False


        def main_data():
            print(Style.BRIGHT + Fore.YELLOW)
            archive_file = input("\nВведите адрес архива ")
            # делаем проверку рассширенния взламываемого файла
            if not archive_file.endswith('.zip') and not archive_file.endswith('.rar'):
                # if not any(map(archive_file.endswith, ('.zip', '.rar'))):
                print(Style.BRIGHT + Fore.RED)
                print(
                    "Вы указали неверный файл для взлома. Файл не имеет расширения 'zip' или 'rar' ")
                main_data()

            password_list = input("Введите адресс словаря ")

            # Инициализируем
            if (archive_file.endswith('.zip')):
                file_for_breaking = zipfile.ZipFile(archive_file)
            elif (archive_file.endswith('.rar')):
                file_for_breaking = rarfile.RarFile(archive_file)

            # подсчитываем количесвто слов в словаре
            cnt = len(list(open(password_list, 'rb')))

            print("Количество паролей в данном словаре ", cnt)

            if crack_password(password_list, file_for_breaking) is False:
                print(Style.BRIGHT + Fore.RED)
                print("\nПароль не найден. Попробуйте другой словарь ")
                main_data()


        main_data()

        def console_picture():
            print(Style.BRIGHT + Fore.RED)
            print("   ########   ########  ##      ##   #######   ########    ######## ")
            print("   ########   ########  ##      ##   ##    ##  ##          ######## ")
            print("   ##    ##   ##    ##  ##     ###   ########  ########       ##  ")
            print("   ##    ##   ########  ##  ##  ##   ##    ##  ##             ##  ")
            print("   ##    ##   ##        ## #    ##   ########  ########       ##  ")
            print("   ##    ##   ##        ##      ##   #######   ########       ##  ")
            print()
            print()
            print("   ########      ###    ##      ##   ########   ##      ##  ########     @@ ")
            print("   ##           #####   ##      ##   ##    ##   ##      ##  ########     @@ ")
            print("   ######      ##   ##  ##########   ##    ##   ##      ##     ##        @@ ")
            print("   ##    ##   ##     ## ##      ##   ##    ##   ##    ####     ##        @@ ")
            print("   ########   ######### ##      ##   ##    ##   ##  ##  ##     ##        @@ ")
            print("   ######     ##     ## ##      ##  ##########  ## #    ##     ##           ")
            print("                                    ##      ##  ##      ##     ##        @@ ")
            print()
            print()
            print()


        console_picture()


        wordTitle = '          Программа для взлома запароленных zip архивов '
        # создаем эффект печатания текста (текст выводиться с задержкой)
        for i in wordTitle:
            print(i.upper(), end="")
            time.sleep(0.03)


        def crack_password(password_list, file_for_breaking):
            indx = 0
            cnt = len(list(open(password_list, 'rb')))
            # открываем файл (with open() as file: - пишем так, чтобы потом не писать комманду закрытия файла (close()). rb открытие в двоичном режиме )
            with open(password_list, 'rb') as file:
                for line in file:
                    for word in line.split():
                        # вычисляем в процентном соотношении количество пребранных паролей
                        x = (indx+1)/cnt * 100
                        # отсекаем цифры после запятой до 2-х, чтоб не получалось вроде такого: 0.9834539503%
                        x = float('{:.2f}'.format(x))
                        print(
                            f'Количество перебранных паролей {indx} ----- Процент перебранных паролей {x}\r', end="")  # подсчитываем количество перебранных паролей. Вывод текста в одну строку с затиранием предыдущего
                        try:
                            indx += 1
                            # pwd: если zip-файл зашифрован, передайте пароль в этом аргументе (по умолчанию: None) .
                            file_for_breaking.extractall(pwd=word)
                            print("\n")
                            print("Пароль найден в строке: ", indx)
                            # Декодирует байтстроку в строку.
                            print("Пароль: ", word.decode())
                            # После нахождения пароля, спрашиваем про желание продолжить взламывать пароли
                            continue_work = input(
                                "Хотите продолжить? Если да, то нажмите букву 'д', если хотите выйти в главное меню нажмите - 0:_")
                            if (continue_work == 'д'):
                                main_data()
                                # return True
                            elif (continue_work == '0'):                                
                                startProgramm()
                            else:
                                return True

                        except:

                            continue
            return False


        def main_data():
            print(Style.BRIGHT + Fore.YELLOW)
            zip_file = input("\nВведите адрес zip архива ")
            # делаем проверку рассширенния взламываемого файла
            if zip_file.endswith('.zip') == False:
                print(" Вы указали неверный файл для взлома. Файл не имеет расширения 'zip' ")
                main_data()

            password_list = input("Введите адресс словаря ")

            # Инициализируем
            file_for_breaking = zipfile.ZipFile(zip_file)

            # подсчитываем количесвто слов в словаре
            cnt = len(list(open(password_list, 'rb')))

            print("Количество паролей в данном словаре ", cnt)

            if crack_password(password_list, file_for_breaking) == False:
                print("\nПароль не найден. Попробуйте другой словарь ")
                main_data()


        main_data()

    def import7z():
        def console_picture():
            print(Style.BRIGHT + Fore.WHITE)
            print("   ########   ########  ##      ##   #######   ########    ######## ")
            print("   ########   ########  ##      ##   ##    ##  ##          ######## ")
            print("   ##    ##   ##    ##  ##     ###   ########  ########       ##  ")
            print("   ##    ##   ########  ##  ##  ##   ##    ##  ##             ##  ")
            print("   ##    ##   ##        ## #    ##   ########  ########       ##  ")
            print("   ##    ##   ##        ##      ##   #######   ########       ##  ")
            print()
            print()
            print("   ########      ###    ##      ##   ########   ##      ##  ########     @@ ")
            print("   ##           #####   ##      ##   ##    ##   ##      ##  ########     @@ ")
            print("   ######      ##   ##  ##########   ##    ##   ##      ##     ##        @@ ")
            print("   ##    ##   ##     ## ##      ##   ##    ##   ##    ####     ##        @@ ")
            print("   ########   ######### ##      ##   ##    ##   ##  ##  ##     ##        @@ ")
            print("   ######     ##     ## ##      ##  ##########  ## #    ##     ##           ")
            print("                                    ##      ##  ##      ##     ##        @@ ")
            print()
            print()
            print()


        console_picture()


        wordTitle = '          Программа для взлома запароленных 7z архивов '
        # создаем эффект печатания текста (текст выводиться с задержкой)
        for i in wordTitle:
            print(i.upper(), end="")
            time.sleep(0.03)

        print(Style.BRIGHT + Fore.RED)
        print()
        print("Предупрежение!")
        print()
        print("""Файлы с таким расширением очень устойчивы к атакам грубой силы, 
        поэтому перебор паролей будет происходить крайне низко!!!""")

        stopwatch = Stopwatch(2)  # 2 это десятична точность для секундомера


        def crack_password(password_list, file_for_breaking):
            indx = 0
            cnt = len(list(open(password_list, 'rb')))
            # открываем файл (with open() as file: - пишем так, чтобы потом не писать комманду закрытия файла (close()). rb открытие в двоичном режиме )
            with open(password_list, 'rb') as file:
                stopwatch.restart()
                for line in file:
                    for word in line.split():
                        # вычисляем в процентном соотношении количество пребранных паролей
                        x = (indx+1)/cnt * 100
                        # отсекаем цифры после запятой до 2-х, чтоб не получалось вроде такого: 0.9834539503%
                        x = float('{:.2f}'.format(x))
                        print(
                            f'Количество перебранных паролей {indx} ----- Процент перебранных паролей {x} ---- Прошло времени {str(stopwatch)}\r', end="")  # подсчитываем количество перебранных паролей. Вывод текста в одну строку с затиранием предыдущего
                        try:
                            indx += 1
                            with py7zr.SevenZipFile(file_for_breaking, password=word.decode('utf8')) as z:
                                z.extractall()
                            print("\n")
                            print(Style.BRIGHT + Fore.GREEN)
                            print("Пароль найден в строке: ", indx)
                            # Декодирует байтстроку в строку.
                            print("Пароль: ", word.decode())
                            stopwatch.reset()  # сбрасываем счетчик на 0
                            # После нахождения пароля, спрашиваем про желание продолжить взламывать пароли
                            continue_work = input(
                                "Хотите продолжить? Если да, то нажмите букву 'д', если хотите выйти в главное меню нажмите - 0:_")
                            if (continue_work == 'д'):
                                main_data()
                                # return True
                            elif (continue_work == '0'):                                
                                startProgramm()
                            else:
                                return True

                        except:

                            continue
            return False


        def main_data():
            print(Style.BRIGHT + Fore.YELLOW)
            archive_file = input("\nВведите адрес 7z архива ")
            # делаем проверку рассширенния взламываемого файла
            if not archive_file.endswith(('.7z')):
                print(Style.BRIGHT + Fore.RED)
                print("Вы указали неверный файл. Файл не имеет расширения '7z' ")
                main_data()

            password_list = input("Введите адресс словаря ")

            file_for_breaking = archive_file

            # подсчитываем количесвто слов в словаре
            cnt = len(list(open(password_list, 'rb')))

            print("Количество паролей в данном словаре ", cnt)

            if crack_password(password_list, file_for_breaking) == False:
                print("\nПароль не найден. Попробуйте другой словарь ")
                main_data()


        main_data()

    def importMSOffice():
        # для созлания разноцветного текста в программе. Необходимо установить (pip install colorama)
        from colorama import init, Fore, Back, Style
        init()


        def console_picture():
            print(Style.BRIGHT + Fore.CYAN)
            print("   ########   ########  ##      ##   #######   ########    ######## ")
            print("   ########   ########  ##      ##   ##    ##  ##          ######## ")
            print("   ##    ##   ##    ##  ##     ###   ########  ########       ##  ")
            print("   ##    ##   ########  ##  ##  ##   ##    ##  ##             ##  ")
            print("   ##    ##   ##        ## #    ##   ########  ########       ##  ")
            print("   ##    ##   ##        ##      ##   #######   ########       ##  ")
            print()
            print()
            print("   ########      ###    ##      ##   ########   ##      ##  ########     @@ ")
            print("   ##           #####   ##      ##   ##    ##   ##      ##  ########     @@ ")
            print("   ######      ##   ##  ##########   ##    ##   ##      ##     ##        @@ ")
            print("   ##    ##   ##     ## ##      ##   ##    ##   ##    ####     ##        @@ ")
            print("   ########   ######### ##      ##   ##    ##   ##  ##  ##     ##        @@ ")
            print("   ######     ##     ## ##      ##  ##########  ## #    ##     ##           ")
            print("                                    ##      ##  ##      ##     ##        @@ ")
            print()
            print()
            print()


        console_picture()


        wordTitle = '          Программа для взлома запароленных документов (word, exel, ppt) '
        # создаем эффект печатания текста (текст выводиться с задержкой)
        for i in wordTitle:
            print(i.upper(), end="")
            time.sleep(0.03)

        stopwatch = Stopwatch(2)  # 2 это десятична точность для секундомера
        decrypted = io.BytesIO()  # для декодирования файлов с расширением docx, xlsx


        def crack_password(password_list, file_for_breaking):

            indx = 0
            cnt = len(list(open(password_list, 'rb')))
            # открываем файл (with open() as file: - пишем так, чтобы потом не писать комманду закрытия файла (close()). rb открытие в двоичном режиме )
            with open(password_list, 'rb') as file:
                stopwatch.restart()
                for line in file:
                    for word in line.split():
                        # вычисляем в процентном соотношении количество пребранных паролей
                        x = (indx+1)/cnt * 100
                        # отсекаем цифры после запятой до 2-х, чтоб не получалось вроде такого: 0.9834539503%
                        x = float('{:.2f}'.format(x))
                        print(
                            f'Количество перебранных паролей {indx} ----- Процент перебранных паролей {x} ---- Прошло времени {str(stopwatch)}\r', end="")  # подсчитываем количество перебранных паролей. Вывод текста в одну строку с затиранием предыдущего
                        try:
                            indx += 1
                            # password если файл зашифрован, передайте пароль в этом аргументе (по умолчанию: None) .
                            file_for_breaking.load_key(password=word.decode('utf8'))
                            # для работы с файлами с расширениями docx и xlsx
                            file_for_breaking.decrypt(decrypted)
                            print("\n")
                            print(Style.BRIGHT + Fore.GREEN)
                            print("Пароль найден в строке: ", indx)
                            # Декодирует байтстроку в строку.
                            print("Пароль: ", word.decode())
                            stopwatch.reset()  # сбрасываем счетчик на 0
                            # После нахождения пароля, спрашиваем про желание продолжить взламывать пароли
                            print(Style.BRIGHT + Fore.YELLOW)
                            continue_work = input(
                                "Хотите продолжить? Если да, то нажмите букву 'д', если хотите выйти в главное меню нажмите - 0:_")
                            if (continue_work == 'д'):
                                main_data()
                                # return True
                            elif (continue_work == '0'):                                
                                startProgramm()
                            else:
                                return True

                        except:

                            continue
            return False


        def main_data():
            print(Style.BRIGHT + Fore.YELLOW)
            code_file = input("\nВведите адрес запароленного документа ")
            # # делаем проверку рассширенния взламываемого файла
            # if not any(map(code_file.endswith, ('.doc', '.docx', '.xlsx', '.rtf'))):
            #     print(Style.BRIGHT + Fore.RED)
            #     print(
            #         "Вы указали неверный файл для взлома. Файл не является документом MSOffice")
            #     main_data()
            # делаем проверку рассширенния взламываемого файла
            if any(map(code_file.endswith, ('.docx', '.xlsx', '.rtf', '.pptx'))):
                print(Style.BRIGHT + Fore.RED)
                print(
                    """Файлы с таким расширением очень устойчивы к атакам грубой силы, 
        поэтому перебор паролей будет происходить крайне низко!!!""")
            print(Style.BRIGHT + Fore.YELLOW)
            password_list = input("Введите адресс словаря ")

            # Инициализируем
            code_file = open(code_file, 'rb')
            file_for_breaking = msoffcrypto.OfficeFile(code_file)
            # print(file_for_breaking.file)

            # подсчитываем количесвто слов в словаре
            cnt = len(list(open(password_list, 'rb')))

            print("Количество паролей в данном словаре ", cnt)

            if crack_password(password_list, file_for_breaking) == False:
                print(Style.BRIGHT + Fore.RED)
                print("\nПароль не найден. Попробуйте другой словарь ")
                main_data()


        main_data()

    def generator():

        from itertools import product  # библиотека, которая выводит все возможные комбинации из введенных пользователем данных

        UserData = input('Введите данные для создания словаря (пример: 1234 . Из этих цифр будет создан словарь): ')
        lenghthMin = int(input('Введите минимальную длину значения/слова: '))
        lenghtMax = int(input('Введите максимальную длину значения(слова): '))

        meaning1 ='' #сюда добавляется каждое новое созданое слово (если из букв) или значение (если пользователь в UserData ввел цифры) 
        sumMeaning = []# сюда записывються все возможные слова /значения из того что ввел пользователь в UserData (создается список)

        for k in range(lenghthMin, lenghtMax+1): #Функция range() возвращает последовательность чисел между заданным начальным целым числом (lenthMin) и конечным целым числом (lenthMax) +1 чтоб получилось число lenthMax иначе на 1 меньше будет число
                for i in product(UserData, repeat=k): # проходим циклом по введенным данным от пользователя и записываем все новые слова/значения в meaning1 
                    meaning1 = ''.join(i)
                    sumMeaning.append(meaning1) # здесь суммируем все новые знаения/слова , т.к. в meaning1 при каждом проходе информация затирается новым значением
            
        exitWords = "\n".join(sumMeaning) # преобразуем полученный список sumMeaning в строку (с переносами - \n на новую строчку значений/слов) и записываем в exitWords

        pathToFile = input('Введите путь куда Вы хотите записать свой файл (в конце пути поставьте \и напишите название своего словаря с расширением txt ): ')

        with open(pathToFile, 'w') as fileUser: # создаем новый файл в папке со скриптом под названием dicton.txt, куда записываем все что получилось от генерации 
            fileUser.write(exitWords)

        continue_work = input("Словарь создан. Хотите продолжить? Если да, то нажмите букву 'д', если хотите выйти в главное меню нажмите - 0:_")
        if (continue_work == 'д'):
            generator()
        elif (continue_work == '0'):                                
            startProgramm()
        else:
            True


    def downloadModul(): # при запуске функции автоматически запускается установка всех необходимых модулей
        from os import system
        system("pip install psutil")
        system("pip install unrar")
        system("pip install msoffcrypto-tool")
        system("pip install py7zr")
        system("pip install stopwatch.py")
        system("pip install colorama")


    if choose =='1':
        importRar()
    elif choose == "2":
        import7z()
    elif choose == "3":
        importMSOffice()
    elif choose == "4":
        generator()
    elif choose == "5":
        downloadModul()
    else:
        print("Вы ничего не выбрали. Попробуйте снова")

startProgramm()