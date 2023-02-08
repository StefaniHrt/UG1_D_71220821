kalimat=input("Kalimat yang ingin diteliti :")
kata=input("kata yang dicari :")
hasil=0
a=kalimat.split()
for i in range(len(a)):
    if kata in a:
        hasil=a.count(kata)
print("Jumlah kata yang dicari :",hasil)