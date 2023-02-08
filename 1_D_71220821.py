print("====================KASIR====================")
harga=input("Harga Barang :")
beli=input("Apakah anda membeli barang lagi? [yes/no] :")
if beli=="yes":
    harga
    beli
elif beli=="no":
    total=sum(harga)
    print("TOTAL BELANJA :", total)
else :
    print("INVALID")