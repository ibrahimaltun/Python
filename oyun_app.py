from os import system
from random import randint


class Silah():
    def __init__(self, isim: str, damage: int):
        self.__isim = isim
        self.__damage = damage

    def vur(self, rakip):
        rakip.setCan(rakip.getCan() - self.__damage)
        self.__damage -= 1

    def getIsim(self):
        return self.__isim

    def getDamage(self):
        return self.__damage

class Karakter():
    def __init__(self, can: int, silah: Silah):
        self.__silah = silah
        self.__can = can

    def vur(self, rakip):
        self.__silah.vur(rakip)

    def getCan(self):
        return self.__can

    def setCan(self, yeniCan:int):
        self.__can = yeniCan

    def getSilahIsim(self):
        return self.__silah.getIsim()

    def getDamage(self):
        return self.__silah.getDamage()

class Dusman(Karakter):
    pass

class Oyuncu(Karakter):
    def __init__(self, isim:str, can:int, silah:Silah):
        Karakter.__init__(self, can, silah)
        self.__isim = isim

    def getIsim(self):
        return self.__isim

def Main():
    dusmanlar = []

    for i in range(10):
        dusmanlar.append(Dusman(randint(30, 50), Silah("Bıçak",randint(10,20))))
    isim = input("Oyuncu adınız giriniz : ")
    guc = input("Oyuncunun gücünü giriniz(Önerilen >200) : ")
    silah = input("Oyuncunun silah adını giriniz : ")
    damage = input("Oyuncunun silah gücünü giriniz(Önerilen >45) : ")

    oyuncu = Oyuncu(isim, int(guc), Silah(silah, int(damage)))

    while True:
        system("cls")
        print("Oyuncu :  {} ------- Can : {} -------  Silah : {} -------  Damage : {} ".format(oyuncu.getIsim(),oyuncu.getCan(),oyuncu.getSilahIsim(),oyuncu.getDamage()))
        print("===========================================================================")

        for sayi,i in enumerate(dusmanlar):

            print("No : {} ----  Düşman Can : {} -------  Düşman Damage : {} -------  Düşman Silah : {} ".format(sayi, i.getCan(),i.getDamage(),i.getSilahIsim()))
        print("========================================================================")

        secim = input("Saldırılacak düşmanı seçiniz : ")
        dusman = dusmanlar[int(secim)]
        oyuncu.vur(dusman)

        if dusman.getCan() <= 0:
            dusmanlar.remove(dusman)
            if not dusmanlar:
                print("Tebrikler, Kazandınız.")
                quit() #veya break yazılabilir.

        if dusmanlar: # eğer dusmanlar listesinde en az bir öğre var is
            dusmanlar[randint(0, len(dusmanlar) - 1)].vur(oyuncu)

            if oyuncu.getCan() <= 0:
                print("Oyunu kaybettiniz...")
                quit()


if __name__ == "__main__":
    Main()
