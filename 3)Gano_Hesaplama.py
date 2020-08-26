# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:20:56 2020

@author: bykzi
"""



vize = input("Vize notunuzu giriniz : ")
final = input("Final notunuzu giriniz : ")

ortalama = (float(vize)*0.4) + (float(final)*0.6)

if int(final) < 30:
    print("Final barajından kaldınız, notunuz FF \nBütte görüşürüz...")
    
else:
    
    if ortalama > 79:
            print("Ortalamanız : {} \nHarf notunuz : AA".format(ortalama))
        
    elif ortalama > 69:
            print("Ortalamanız : {} \nHarf notunuz :  BA".format(ortalama))
            
    elif ortalama > 59:
            print("Ortalamanız : {} \nHarf notunuz :  BB".format(ortalama))
            
    elif ortalama > 49:
            print("Ortalamanız : {} \nHarf notunuz :  CB".format(ortalama))
            
    elif ortalama > 39:
            print("Ortalamanız : {} \nHarf notunuz :  CC".format(ortalama))
            
    else:
            print("Ortalamanız : {} \nHarf notunuz :  FF\nKaldınız...".format(ortalama))

    
    
    
    