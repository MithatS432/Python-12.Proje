import threading
import multiprocessing
import asyncio
import time

# ------------------------
# 1. Threading örneği
# ------------------------
def say_geri(sure):
    for i in range(sure, 0, -1):
        print(f"[Thread] Geri sayım: {i}")
        time.sleep(1)

thread = threading.Thread(target=say_geri, args=(3,))
thread.start()

# ------------------------
# 2. Multiprocessing örneği
# ------------------------
def faktoriyel(n):
    sonuc = 1
    for i in range(1, n+1):
        sonuc *= i
    print(f"[Process] {n}! = {sonuc}")

process = multiprocessing.Process(target=faktoriyel, args=(5,))
process.start()

# ------------------------
# 3. Asyncio örneği
# ------------------------
async def bekle_ve_yaz(mesaj, sure):
    await asyncio.sleep(sure)
    print(f"[Async] {mesaj} ({sure} sn sonra)")

async def main_async():
    await asyncio.gather(
        bekle_ve_yaz("Merhaba", 1),
        bekle_ve_yaz("Dünya", 2)
    )

asyncio.run(main_async())

# ------------------------
# 4. Context Manager (with) örneği
# ------------------------
class Dosya:
    def __init__(self, dosya_adi, mod):
        self.dosya_adi = dosya_adi
        self.mod = mod

    def __enter__(self):
        print("[Context Manager] Dosya açılıyor...")
        self.dosya = open(self.dosya_adi, self.mod)
        return self.dosya

    def __exit__(self, exc_type, exc_value, traceback):
        self.dosya.close()
        print("[Context Manager] Dosya kapatıldı.")

with Dosya("log.txt", "w") as f:
    f.write("Python ileri seviye örnek.\n")
