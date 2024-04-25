import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Şifreniz karekterden oluşsun ? "))

password = ""
for i in range(uzunluk):
    password += random.choice(karakterler)
print("Size oluşturduğum şifre : ",password)
