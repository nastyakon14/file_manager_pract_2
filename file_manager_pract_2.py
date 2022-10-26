#!/usr/bin/env python
# coding: utf-8

# In[7]:


import subprocess
import os
import shutil
from sys import platform

# функции позволяющие выполнять операции с файлами


def dir(l,symb):      # функция, позволяющая попадать в нужную директорию
    cd = input('Введите назвние каталога .\n')    
    directory = (l + symb + cd)   # путь к файлу
    files = os.listdir(directory)  # озвращает список, содержащий имена файлов и директорий в каталоге, заданном путем directory
    os.chdir(l + symb + cd)    # изменяет текущий рабочий каталог
    for i in files:
        print(i)
    file = os.chdir(l + symb + cd)   # изменяет текущий рабочий каталог
    return(directory)

def updir(l,symb):   # на каталог выше перемещение
    deldir = l.split(symb)   # разбивает по \
    print(deldir[-1])
    cd = l.split(symb+deldir[-1])   
    print(cd[0])
    return(cd[0])

def delf(l,symb):      # удаление файла
    d = input('Введите путь к файлу для удаления>>')
    os.remove(l + symb + d, dir_fd=None)
    print('готово,файл', d, 'удален из дерриктории:', l)

def deld(l,symb):   # удаление каталога
    d = input('Введите путь к каталогу для удаления>>')
    os.rmdir(l + symb + d)
    print('готово,файл', d, 'удален из дерриктории:', l)

def newf(l,symb):   # создание нового файла
    nf = input('Введите имя и расширение файла>>')
    open(nf, "w")
    print('Файл создан в дерриктории:', l, 'с именем', nf)

def newd(l,symb):   # новый каталог
    print('Введите название паки чтобы создать ее в дериктории:', l)
    nd = input(">>")
    os.mkdir(nd)
    print('готово, папка создана с именем-', nd, 'в дерриктории:', l)

def read(l,symb):   #чтение файла, всего его сожержимого
    print('Введите путь к файлу')
    in_file = input()
    my_file = open(l + symb + in_file)
    my_string = my_file.read()
    print(my_string)
    my_file.close()         
    print('Прочитан файл - ', in_file)

def write(l,symb):   # позволяет сделать запись в файл
    print('Введите путь к файлу')
    in_file = input()
    my_file = open(l + symb + in_file, "a")   #открытие файда на запись
    writing = input('Введите текст\n')   #текст для записи
    my_file.write(writing)   # запись в файл
    my_file.close()
    print('Запись сдедлана в файл - ', in_file)

def copyf(l,symb):    # копирует файл из одного каталога в другой
    path1 = input('Введите путь файла, который нужно скопировать\n')
    path2 = input('Введите путь, куда нужно скопировать\n')
    shutil.copy2(l + symb + path1, l + symb + path2)
    print('Файла скопирован в ', l + symb + path2)

def movef(l,symb):   # перемещение файла из одного каталога в другой
    path1 = input('Введите путь файла, который нужно переместить\n')
    path2 = input('Введите путь, куда нужно переместить\n')
    shutil.move(l + symb + path1, l + symb + path2)
    print('Файла перемещен в ', l + symb + path2)

def renamef(l,symb):    # переименовывает файл
    path1 = input('Введите путь файла, который нужно переименовать\n')   # путь к файлу
    path2 = input('Введите новое имя\n')
    os.rename(l + symb + path1, l + symb + path2)
    print('Файла перемещен в ', l + symb + path2)

def openf(l,symb):
    openf = input('Введите название файла >> ')
    cmd = openf
    subprocess.Popen(cmd, shell=True)
   
#форма записи путей для линукс и виндоус отличается слешами

def __main__():    # позволяет работать на платфомрах линукс и линукс2
    if platform == "linux" or platform == "linux2":
        symb = '/'
        print('введите Полное название католога в виде /home ')
    elif platform == "win32" or platform == "win64":   #для работы с windows
        symb = '\\'
        print('введите Полное название католога в виде C:\ ')
    c=''
    l = input()
    homedir = l   # домашний каталог, первоначальный путь
    print(symb)
    while c != 'stop':
        directory = (l)
        files = os.listdir(directory)
        file = os.chdir(l)
        print('Текущий каталог: ', l)
        print('Домашний каталог: ', homedir)
    # запуск программ или переход в другую директорию
        print('введите комманду')
        c = input()    # команда для оаботы с файлами
        if c == 'help':   # кнопка помощи, выдает перечнь возможных функций
            print("\nвведите dir чтобы перейти в другой каталог либо в католог в этой папке "
                "\nвведите updir чтобы перейти на папку выше "
                "\nвведите lsdir чтобы отобразить содержимое текущей папки "
                "\nдля того чтобы создать файл введите newf, "
                "\nвведите newd чтобы создать папку, "
                "\nвведите delf если хотите удалить файл в катологе>"
                "\nвведите deld если хотите удалить каталог>"
                "\nвведите read чтобы посмотреть содержимое файла"
                "\nвведите write чтобы сделать запись в файл"
                "\nвведите copyf чтобы скопировать файл в другой каталог"
                "\nвведите movef чтобы переместить файл в другой каталог"
                "\nвведите renamef чтобы переименовать файл\n"
                "stop для остановки программы\n",
                l)
        elif c == 'lsdir':   # отобразить содержимое папки
            for i in files:
                print(i)
        elif c == 'dir':   # перейти в другой каталог или каталог в этой папке
            l = dir(l,symb)
        elif c == 'updir':   # на папку выше
            if l == homedir:
                print('!Невозможно подняться выше домашнего каталога!')
            else:
                l = updir(l,symb)
        elif c == 'delf':  # Удаление файла из дерриктории
            delf(l,symb)
        elif c == 'deld':  # Удаление всего каталога из дерриктории
            deld(l,symb)
        elif c == 'newf':   # создание нового файла
            newf(l,symb)
        elif c == 'newd':   # новый каталог
            newd(l,symb)
        elif c == 'read':   # чтение фацла, его содержимое
            read(l,symb)
        elif c == 'write':   # запись в файл
            write(l,symb)
        elif c == 'copyf':     # копирование файла
            copyf(l,symb)
        elif c == 'movef':   # перемещение файла между каталогами
            movef(l,symb)
        elif c == 'renamef':   # переименование имени файла
            renamef(l,symb)
        elif c == 'open':   #открытие файла
            openf(l,symb)
        elif c == 'stop':   # конец работы
            print('Выхожу из программы')
        else:   # ошибка
            print('Введена неверная команда\nОткатываемся\nВведите путь заново')


if __name__ == "__main__":
    __main__()


# In[ ]:




