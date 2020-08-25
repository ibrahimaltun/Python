# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:38:13 2020

@author: bykzi
"""

from random import randint

rast = randint(1,100)
sayac = 0

while True:
    
    sayac += 1
    
    sayi = int(input("1 ile 100 arasında bir değer giriniz : "))
    print("Çıkış için 0 tuşuna basınız...")
    
    if (sayi == 0):
        print("Oyundan çıktınız...")
        break
    
    elif sayi < rast:
        print("Daha büyük bir sayı giriniz.")
        continue
    
    elif sayi > rast:
        print("Daha küçük bir sayı giriniz.")
        continue
    
    else:
        print("Rastgele seçilen sayı : {}".format(rast))
        print("{}. tahminde doğru buldunuz.".format(sayac))
        break
              