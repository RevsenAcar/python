#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boyboy)) hesaplayınız.

import math


boy = float(input("Lutfen boyunuzu giriniz : "))
kilo = int(input ("Lutfen kilonuzu giriniz :"))
vki=kilo/(boy*boy)
print("vücut kitle indeksiniz:",vki)

#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
maas = 50000
zamOrani = 10
zamliMaas = maas + (maas * zamOrani / 100)
print("Zamlı maaşınız:", zamliMaas)

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
sayi1 = int(input("1. Sayıyı Giriniz: "))
sayi2 = int(input("2. Sayıyı Giriniz: "))
sayi3 = int(input("3. Sayıyı Giriniz: "))

enBuyuk = None

if sayi1 > sayi2 and sayi1 > sayi3:
    enBuyuk = sayi1
    print("en büyük sayı : ",enBuyuk)
elif sayi2 > sayi1 and sayi2 > sayi3:
    enBuyuk = sayi2
    print("en büyük sayı : ",enBuyuk)
elif sayi3 > sayi1 and sayi3 > sayi2:
    enBuyuk = sayi3
    print("en büyük sayı : ",enBuyuk)
else:
    print("Lütfen farklı sayılar giriniz")

#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
yaricap = int(input("Dairenin yarıçapını girin: "))
alan = math.pi * yaricap ** 2

cevre = 2 * 3.14 * yaricap
print("Dairenin alanı:", alan)
print("Dairenin çevresi:", cevre)


#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi = int(input ("Lutfen bir sayi giriniz :"))
def is_palindrome(number):
    reverse_number = int(str(number)[::-1])
    return number == reverse_number

if is_palindrome(sayi):
    print("Girdiginiz sayi palindromdur.")
else:
    print("Girdiginiz sayi palindrom degildir.")