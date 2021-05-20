'''
Для адекватного распознавания:
+ кодировки utf-8
+ скрипта unix-системами
+ для случаев работы пользователя в виртуальном окружении
+ для определения версии, под которой был разработан данный скрипт
'''
##! /usr/local/bin/python
# Python 3.8.6
# -*- coding: utf-8 -*-
##! /usr/bin/env python3

# Импортируем нужные нам библиотеки

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
#import threading
import setuptools
from pyfiglet import Figlet
from colorama import Fore, Back, Style

# Просто ляпота :)

Author = 'SlayerLeon'
__name__ = 'Generator For'
f = Figlet(font='slant')
r0 = print(f.renderText(Author))
r1 = print(f.renderText(__name__))



print('Generator of links for Yandex.Disk and Pastebin.com')


# Для скрытия работы Selenium в браузере и ссылка на chromedriver для работы selenium в Chrome Browser

## driver = webdriver.Chrome('C:\\Users\\User\\Desktop\\chromedriver.exe')
username = str(input("PLease, enter your username this PC: \n"))
options = Options()
options.add_argument("headless")
options.headless = True
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(f'C:\\Users\\{username}\\Desktop\\Github\\generator_for_\\chromedriver.exe', options=options)

# ТЕЛО СКРИПТА

# def main(x, event_for_wait, event_for_set):
query = input(str('If you want close is program, then enter Y/y, otherwise N/n? \n'))   # Желаете ли Вы завершить работу с этой программой?
# event_for_wait.wait() # wait for event
# event_for_wait.clear() # clean event for future
# print (x)
# event_for_set.set() # set event for neighbor thread
while (query == 'n') or (query == 'N'):
    service = str(input('Select service (pastebin | yandex.disk):'+'\n'))
    if service == 'yandex.disk':
        loc = 0     # переменная для подсчёта строк ссылок
        # обработчик ошибок при вводе некорректного значения количества ссылок
        try:
            m = int(input('Please, enter quantity of links:'))
        except ValueError:
            # while
            print('Please, enter only one cipher or number')
            m = int(input('Please, enter quantity of links:'))
        finally:
            while loc != m:
                # без последующих символов +-/*!&$#?=w@<> :%\
                chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
                # length - это длина link
                # length = int(input('Length links?'+ '\n'))
                length = 14
                random.shuffle(chars)
                link = ''.join([random.choice(chars) for x in range(length)])
                res1 = str(f'https://yadi.sk/d/{link}')
                res2 = str(f'https://yadi.sk/i/{link}')
                def yc_pluse():
                    ''' '''
                    global loc
                    loc = str(loc)
                    print(loc+' '+'+'+' '+res1+'\n')
                    print(loc+' '+'+'+' '+res2+'\n')
                    loc = int(loc)
                    loc = loc+1

                def yc_minus():
                    ''' '''
                    global loc
                    loc = str(loc)
                    print(loc+' '+'-'+' '+res1+'\n')
                    print(loc+' '+'-'+' '+res2+'\n')
                    loc = int(loc)
                    loc = loc+1

                driver.get(res1)
                driver.get(res2)
                try:
                    yc0 = driver.find_elements_by_class_name('content__centered')
                    if (yc0 == True):
                        yc_pluse()
                    else:
                        yc_minus()
                except NoSuchElementException:
                    yc1 = driver.find_elements(By.XPATH, '//div/div/div/div/div[2]/div[2]')
                    if (yc1 == True):
                        yc_pluse()
                    else:
                        yc_minus()
                except NoSuchElementException:
                    yc2 = driver.find_elements_by_xpath('//div/div/div/div/div[2]/div[2]')
                    if (yc2 == True):
                        yc_pluse()
                    else:
                        yc_minus()
                except NoSuchElementException:
                    yc3 = driver.find_elements(By.CLASS_NAME, 'content__centered')
                    if (yc3 == True):
                        yc_pluse()
                    else:
                        yc_minus()
            else:
                print('ERROR : 00/0_NoSuchElement')

    elif service == 'pastebin':
        col = 0
        # copy construction upper try-except
        n = int(input('Please, enter quantity of links:'))
        while col != int(n):
            chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
            length = 8
            random.shuffle(chars)
            link = ''.join([random.choice(chars) for x in range(length)])
            res0 = str(f'https://pastebin.com/{link}')
##          res1 = str(f'https://pastebin.com/u/{link}'+'\n')
##          Generate link on users
            '''Transition on link at value res1 and work with html'''
            if (res0 != True):
                random.shuffle(chars)
                link = ''.join([random.choice(chars) for x in range(length)])
                res0 = str(f'https://pastebin.com/{link}')
                def pstb_pluse():
                    global col
                    col = str(col)
                    print(col+' '+'+'+' '+res0+'\n')
                    col = int(col)
                    col = col+1
                def pstb_minus():
                    global col
                    col = str(col)
                    print(col+' '+'-'+' '+res0+'\n')
                    col = int(col)
                    col = col+1

                driver.get(res0)
                try:
                    pstb0 = driver.find_elements_by_class_name('username')
                    if (pstb0 == True):
                        pstb_pluse()
                    else:
                        pstb_minus()
                except NoSuchElementException:
                    pstb1 = driver.find_elements(By.XPATH, '//div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]')
                    if (pstb1 == True):
                        pstb_pluse()
                    else:
                        pstb_minus()
                except NoSuchElementException:
                    pstb2 = driver.find_elements_by_class_name('info-top')
                    if (pstb2 == True):
                        pstb_pluse()
                    else:
                        pstb_minus()
                finally:
                    pass
            else:
                print('ERROR : 00/1_NoSuchElement')

                '''
                WRITE SELECTED LINKS IN RESULT
                '''
                '''Eceptions errors'''
                '''
                Сделать возможность работы Selenium в скрытом режиме
                + до тех пор, пока не будет положительного результата
                '''
    else:
        print('ERROR : 01_ServiceNotFound')
    query = input(str('If you want close is program, then enter Y/y, otherwise N/n? \n'))
else:
     if (query == 'y') or (query == 'Y'):
         sys.exit()
     else:
         print('ERROR : 02_UnknownValue')
         print('Please, reset this programm or wait 15 sec')
         time.sleep(15)
         sys.exit()

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
