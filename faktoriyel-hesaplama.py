def faktoriyel (sayi):
    if sayi==0 or sayi==1:
        return 1
    else:
        return sayi* faktoriyel(sayi-1)

sayi= int(input("Lütfen faktöriyeli hesaplanacak sayıyı giriniz: "))
sonuc=faktoriyel(sayi)

print(f"{sayi} sayısının faktöriyeli: {sonuc}")
