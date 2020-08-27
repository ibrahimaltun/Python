# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 08:55:59 2020

@author: bykzi
"""


def daireAlan(yarıcap): 
    alan = 3.14*(float(yarıcap)**2)
    print("Daire Alanı : ",alan)
    return alan

def dikdortgenAlan(gen,yuk):
    alan = float(gen) * float(yuk)
    print("Dikdörtgen Alanı : ",alan)
    return alan

def kareAlan(kenar_u):
    alan = float(kenar_u)**2
    print("Kare Alanı : ",alan)
    return alan

print("""
      
      [1] Daire Alanı Hesapla
      [2] Dikdörtgen Alanı Hesapla
      [3] Kare Alanı Hesapla
      
      [Q] Çıkış
      
      """)
      
secim = input("Yapmak istediğiniz işlemi seçiniz : ")

if secim == "1":
    yarıcap = input("Dairenin yarıçapınızı giriniz : ")
    daireAlan(yarıcap)
    

elif secim == "2":
    gen = input("Dikdörtgenin yüksekliğini giriniz : ")
    yuk = input("Dikdörtgenin genişliğini giriniz : ")
    dikdortgenAlan(gen, yuk)
    
elif secim == "3":
    kenar = input("Karenin bir kenarının uzunluğunu giriniz : ")
    kareAlan(kenar)
    
elif secim == "q" or secim == "Q":
    print("Çıkılıyor...")
    quit()

else:
    print("Lütfen listede ki işlemlerden birini seçiniz..!")
    