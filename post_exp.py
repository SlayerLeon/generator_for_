
# Для адекватного распознавания:
# + кодировки utf-8
# + скрипта unix-системами
# + для случаев работы пользователя в виртуальном окружении
# + для определения версии, под которой был разработан данный скрипт

# ! /usr/local/bin/python
# Python 3.8.6
# chromedriver.exe version
# -*- coding: utf-8 -*-
# ! /usr/bin/env python3
# Импортируем нужные нам библиотеки
import os
import sys
import time
from selenium import *
import random
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException as WDE
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidElementStateException as IESE
from setuptools import *
from threading import Thread
# from loguru import logger
# from numba import njit, prange
import setuptools
from pyfiglet import Figlet
from colorama import Fore, Back, Style
__Author__ = "SlayerLeon"
name = "Generator For"
f = Figlet(font="slant")
r0 = print(f.renderText(__Author__))
r1 = print(f.renderText(name))
print('Generator of links for Yandex.Disk and Pastebin.com')
username = str(input('Please, enter your username this PC: \n'))
options = Options()
options.add_argument('headless')
options.headless = True
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(f'C:\\Users\\{username}\\chromedriver.exe', options=options)


loc = 0


def QoL():

    while True:
        try:
            global m
            m = int(input('Please, enter quantity of links: '))
            if m <= 0:
                print('Value Error')
            else:
                break
        except Exception:
            print('Value Error')


def decor2(f2):
    def wrapper2(res0):
        global loc
        loc = str(loc)
        f2(res0)
        loc = int(loc)
        loc = loc+1
    return wrapper2

@decor2
def ydp(res1, res2):
    '''
    Взаимодействие с положительным результатом yandex.disk
    '''
    print(loc + ' ' + '+' + ' ' + res1 + '\n')
    print(loc + ' ' + '+' + ' ' + res2 + '\n')
@decor2
def ydm(res1, res2):
    '''
    Нежелательный результат yandex.disk
    '''
    print(loc + ' ' + '-' + ' ' + res1 + '\n')
    print(loc + ' ' + '-' + ' ' + res2 + '\n')

@decor2
def pstbp(res0):
    '''
    Взаимодействие с положительным результатом pastebin.com
    '''
    print(loc + ' ' + '+' + ' ' + res0 + '\n')

@decor2
def pstbm(res0):
    '''
    Нежелательный результат pastebin.com
    '''
    print(loc + ' ' + '-' + ' ' + res0 + '\n')

def start(loc):
    query = input(str('If you want close is program, then enter Y/y, otherwise N/n? \n'))

    while True:
        try:
            service = str(input('Select service (pastebin | yandex.disk):' + '\n'))
            break
        except Exception:
            service = str(input('Select service (pastebin | yandex.disk):' + '\n'))
    QoL()
    if service == 'yandex.disk':
        while loc != m:
            yandex()
    elif service == 'pastebin':
        while loc != m:
            pastebin()
    else:
        raise ValueError

def decor(f):
    def wrapper0():
        #   while loc != int(m):
        chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        length = 8 # for yandex is value equal 14
        random.shuffle(chars)
        link = ''.join([random.choice(chars) for x in range(length)])
        f(link)
    return wrapper0

@decor
def pastebin(link):
    '''
    Данная функция проверяет только одну ссылку для pastebin по 4 параметрам
    '''
    res0 = str(f'https://pastebin.com/{link}')
    # pstbp(res0)
    # pstbm(res0)
    driver.get(res0)
    try:
        pstb0 = driver.find_elements_by_class_name('username')
        pstb1 = driver.find_elements(By.XPATH, '//div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/h1')
        pstb2 = driver.find_elements(By.XPATH, '//div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/h1')
        pstb3 = driver.find_elements_by_class_name('info-top')
        if ((pstb0 or pstb1 or pstb2 or pstb3) == True):
            pstbp(res0)
        else:
            pstbm(res0)
    except NoSuchElementException:
        print('ERROR : 00/1_NoSuchElement')

@decor
def yandex(link):
    res1 = str(f'https://yadi.sk/d/{link}')
    res2 = str(f'https://yadi.sk/i/{link}')
    driver.get(res1)
    driver.get(res2)
    try:
        yd0 = driver.find_elements_by_class_name('content__centered')
        yd1 = driver.find_elements(By.XPATH, '//div/div/div/div/div[2]/div[2]')
        yd2 = driver.find_elements_by_xpath('//div/div/div/div/div[2]/div[2]')
        yd3 = driver.find_elements(By.CLASS_NAME, 'content__centered')
        '''
        Check variable res1 on exists
        '''
        if ((yd0 or yd1 or yd2 or yd3) == True):
            ydp(res1)
        else:
            ydm(res1)
        '''
        Check variable res2 on exists
        '''
        if ((yd0 or yd1 or yd2 or yd3) == True):
            ydp(res2)
        else:
            ydm(res2)
    except NoSuchElementException:
        print('ERROR : 00/0_NoSuchElement')

start(loc)






#     if (yc1 == True):
#         yc_pluse()
#     else:
#         yc_minus()
# except NoSuchElementException:
#     if (yc2 == True):
#         yc_pluse()
#     else:
#         yc_minus()
# except NoSuchElementException:
#     if (yc3 == True):
#         yc_pluse()
#     else:
#         yc_minus()
#
# ТЕЛО СКРИПТА
#
#
# МНОГОПОТОЧНОСТЬ
# def thread0(x, event_for_wait, event_for_set):
#
# event_for_wait.wait() # wait for event
# event_for_wait.clear() # clean event for future
# print (x)
# event_for_set.set() # set event for neighbor thread
#
#         res2 = str(fhttps://yadi.sk/d/{link})
#         res3 = str(fhttps://yadi.sk/i/{link})
#
#         yc_pluse()
#         yc_minus()
#         driver.get(res2)
#         driver.get(res3)
#         try:
#             yc0 = driver.find_elements_by_class_name(content__centered)
#             if (yc0 == True):
#                 yc_pluse()
#             else:
#                 yc_minus()
#         except NoSuchElementException:
#             yc1 = driver.find_elements(By.XPATH, //div/div/div/div/div[2]/div[2])
#             if (yc1 == True):
#                 yc_pluse()
#             else:
#                 yc_minus()
#         except NoSuchElementException:
#             yc2 = driver.find_elements_by_xpath(//div/div/div/div/div[2]/div[2])
#             if (yc2 == True):
#                 yc_pluse()
#             else:
#                 yc_minus()
#         except NoSuchElementException:
#             yc3 = driver.find_elements(By.CLASS_NAME, content__centered)
#             if (yc3 == True):
#                 yc_pluse()
#             else:
#                 yc_minus()
#         else:
#             print(ERROR : 00/0_NoSuchElement)
#
#         res0 = str(fhttps://pastebin.com/{link})
#         res1 = str(fhttps://pastebin.com/u/{link}+\n)
#
#      Generate link on users
#         Transition on link at value res1 and work with html
#         if (res0 != True):
#             random.shuffle(chars)
#             link = .join([random.choice(chars) for x in range(length)])
#             res0 = str(fhttps://pastebin.com/{link})
#
#             driver.get(res0)
#             try:
#                 pstb0 = driver.find_elements_by_class_name(username)
#                 if (pstb0 == True):
#                     pstb_pluse()
#                 else:
#                     pstb_minus()
#             except NoSuchElementException:
#                 pstb1 = driver.find_elements(By.XPATH, //div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1])
#                 if (pstb1 == True):
#                     pstb_pluse()
#                 else:
#                     pstb_minus()
#             except NoSuchElementException:
#                 pstb2 = driver.find_elements_by_class_name(info-top)
#                 if (pstb2 == True):
#                     pstb_pluse()
#                 else:
#                     pstb_minus()
#             finally:
#                 pass
#         else:
#             print(ERROR : 00/1_NoSuchElement)
#
#             WRITE SELECTED LINKS IN RESULT
#
#             Eceptions errors
#
#             Сделать возможность работы Selenium в скрытом режиме
#             + до тех пор, пока не будет положительного результата
#
#
# query = str(input(If you want close is program, then enter Y/y, otherwise N/n? \n))
# while (query == n) or (query == N):
# #   <ОСНОВНОЙ КОД> main0()
#     main0()
# else:
#     if (query == y) or (query == Y):
#         sys.exit()
#     else:
#         print(ERROR : 02_UnknownValue)
#         print(Please, reset this programm or wait 15 sec)
#         time.sleep(15)
#         sys.exit()

#
# Подумать над оформлением query в коде
#
# query = input(str(If you want close is program, then enter Y/y, otherwise N/n? \n))
# # Желаете ли Вы завершить работу с этой программой?
# if __name__ == __main__:
#     pass
#
# МНОГОПОТОЧНОСТЬ
# #init Event
# ev1 = threading.Event()
# ev2 = threading.Event()
# ev3 = threading.Event()
# ev4 = threading.Event()
#
# #init Thread
# th1 = threading.Thread(target=main, args=(0, ev1, ev2))
# th2 = threading.Thread(target=main, args=(1, ev2, ev3))
# th3 = threading.Thread(target=main, args=(2, ev3, ev4))
# th4 = threading.Thread(target=main, args=(3, ev4, ev1))
#
# # start threads
# th1.start()
# th2.start()
# th3.start()
# th4.start()
#
# ev1.set() # initiate the first event
#
# # join threads to the main thread
# th1.join()
# th2.join()
# th3.join()
# th4.join()
#
# /html/body/div[1]/div[2]/div[1]/div[2]/div[1] до Not Found #404
# /html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/h1 до username
# /html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/h1 до username
# pstb1 = driver.find_elements(By.XPATH, //div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1])
#
# if (pstb11 == True) or (pstb10 == True) or (pstb2 == True):
#     pstb_pluse()
# else:
#     pstb_minus()
#
# def main0():
# #
#     loc = 0     # переменная для подсчёта строк ссылок
#     service = str(input(Select service (pastebin | yandex.disk):+\n))
#     # СЮДА РАЗВЕРНУТЬ main1()
#     if service == yandex.disk:
#         main1(m)
#         yc_main2()
#     elif service == pastebin:
#         main1(m)
#         pstb_main2()
#     else:
#         print(ERROR : 01_ServiceNotFound)
#     query = input(str(If you want close is program, then enter Y/y, otherwise N/n? \n))
#
# #Function and Procedure
# def main1(m):
#
#
#
#     try:
#         m = int(input(Please, enter quantity of links:))
#     except ValueError:
#         while m<=0:
#             print(Please, enter only one cipher or number)
#             m = int(input(Please, enter quantity of links:))
#     finally:
#         if service == yandex.disk:
#             yc_main2()
#         elif service == pastebin:
#             pstb_main2()
#         else:
#             pass
#     return m
#
# _________________________________________________________
# def pstb_main2():
#     while loc != int(m):
#         chars = list(abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890)
#         length = 8
#         random.shuffle(chars)
#         link = .join([random.choice(chars) for x in range(length)])
#
# _______________________________________________________
#
#__________________________________________________________
# def yc_main2():
#     while loc != int(m):
#         # без последующих символов +-/*!&$#?=w@<> :%\
#         chars = list(abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890)
#         # length - это длина link
#         # length = int(input(Length links?+ \n))
#         length = 14
#         random.shuffle(chars)
#         link = .join([random.choice(chars) for x in range(length)])

# _________________________________________________________
#
# def yc_pluse(loc):
#
#     Взаимодействие с положительным результатом yandex.disk
#
#     loc = str(loc)
#     print(loc+ +++ +res1+\n)
#     print(loc+ +++ +res2+\n)
#     loc = int(loc)
#     loc = loc+1
# def yc_minus(loc):
#
#     Нежелательный результат yandex.disk
#
#     loc = str(loc)
#     print(loc+ +-+ +res1+\n)
#     print(loc+ +-+ +res2+\n)
#     loc = int(loc)
#     loc = loc+1
# def pstb_pluse(loc):
#
#     Взаимодействие с положительным результатом pastebin.com
#
#     loc = str(loc)
#     print(loc+ +++ +res0+\n)
#     loc = int(loc)
#     loc = loc+1
#
# def pstb_minus(loc):
#
#     Нежелательный результат pastebin.com
#
#     loc = str(loc)
#     print(loc+ +-+ +res0+\n)
#     loc = int(loc)
#     loc = loc+1
