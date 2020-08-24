# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:39:10 2020

@author: bykzi
"""

class HesapMak(object):
    
    def __init__(self, sayi1, sayi2):
        
        self.deger1 = sayi1
        self.deger2 = sayi2
        
    def Toplama(self):
            
        return self.deger1 + self.deger2
        
    def Carpma(self):
            
        return self.deger1 * self.deger2
        
    def Bolme(self):
            
        return self.deger1 / self.deger2
        
    def Cikarma(self):
            
        return self.deger1 - self.deger2
        

print("""
      
      (1) Toplama
      (2) Çarpma
      (3) Bölme
      (4) Çıkarma
      
      """)
      
seciminiz = input("Bir işlem seçiniz : ")

deger1  = int(input("1. Sayıyı giriniz : "))
deger2 = int(input("2. Sayıyı giriniz : "))

islem = HesapMak(deger1, deger2)

if seciminiz == "1":
    toplama_sonuc = islem.Toplama()
    print("Toplama Sonucu : {}".format(toplama_sonuc))

elif seciminiz == "2":
    çarpma_sonuc = islem.Carpma()
    print("Çarpma Sonucu : {}".format(çarpma_sonuc))

elif seciminiz == "3":
    bölme_sonuc = islem.Bolme()
    print("Bölme Sonucu : {}".format(bölme_sonuc))

elif seciminiz == "4":
    cıkarma_sonuc = islem.Cikarma()
    print("Çıkarma Sonucu : {}".format(cıkarma_sonuc))
    
else:
    print("Lütfen ekrandaki işlemlerden biriniz seçiniz...!")













