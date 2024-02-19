# import threading
import time
#
# n = 0
# lock = threading.Lock()
# sem = threading.Semaphore()
#
#
# def s():
#     sem.acquire()
#     global n
#     a = n + 1
#     lock.acquire()
#     time.sleep(1)
#     lock.release()
#     print(a)
#     sem.release()
#
#
# if __name__ == '__main__':
#     p1 = threading.Thread(target=s)
#     p2 = threading.Thread(target=s)
#
#     p1.start()
#     p2.start()

# import asyncio
#
#
# async def f():
#     print(1)
#
#     await asyncio.sleep(1)
#     print(2)
#
# import requests
# from bs4 import BeautifulSoup as bs
#
#
# async def f1():
#     r = requests.get('https://youtube.com')
#     html = bs(r.text, 'html.parser')
#
#     data = html.find_all('div')
#     print(data)
#
#
# async def g():
#     r = requests.get('https://wikipedia.com')
#     html = bs(r.text, 'html.parser')
#
#     data = html.find_all('div')
#     print(data)
#
#
# async def f4():
#     await asyncio.gather(f1(), g())
#
# asyncio.run(f4())


# створити дві функції-корутини роботи з файлами. Перша має створювати файл і записувати 100 строк. Друга читати довільний файл і виводити його строки
# в асинхроному режимі викликати ці дві функції

# функції які парсять різні сайти і виводять їх код

