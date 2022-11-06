import os
import pandas as pd
import csv
import json

booksDate = "books.csv"

def ustuneYaz():
    kitapAdi = input("Kitap Adı: ")
    if len(kitapAdi) > 15:
        print("Kitap adı en az 15 karakter içermelidir.")
    else:
        yazar = input("Yazar: ")
        yayinevi = input("Yayınevi: ")
        sayfa_sayisi = input("Sayfa Sayısı: ")
        okumaZamani = input("Bitirme Tarihi: ")
        fiyat = input("Fiyat: ")
        result = open(booksDate, "a",encoding='utf-8')
        
        result.write(f'\n{kitapAdi}, {yazar}, {yayinevi}, {sayfa_sayisi}, {okumaZamani}, {fiyat}')
        result.close()
    return ""

def delete():
    indexNo = int(input("İndex No: "))
    with open(booksDate, "r+", encoding="utf-8") as f:
        veri = f.readlines()
        veri.pop(indexNo)
        with open(booksDate, "w", encoding="utf-8") as f:
            f.writelines(veri)
            
    return " "
def okut():
    data = pd.read_csv(booksDate)
    get_data = pd.DataFrame(data)
    print(get_data)
    return " " 
yardimListesi = ["ekle | listeye kitap ekler",
                "sil | kitabı listeden siler",
                "listele | kitapları sıralı listeler"]
def yardim():
    print("\t --YARDIM--")
    for i in yardimListesi:
        print("\t", i)
    return " "
    
def default():
    return ""
komutlar = {
    "ekle": ustuneYaz,
    "listele": okut,
    "sil": delete
    }
def switch(case):
    return komutlar.get(case, default)()
while True:
    title = lambda: os.system("title Simple Book Listing App by Burak Y.")
    title()
    komut = input("~#")
    print(switch(komut))