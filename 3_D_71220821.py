string=""
a=int(input("Masukkan Angka :"))
b=a
while b >= 0:
    c=b
    while c>0:
        string=string+" "
        c=c-1
    kiri=1
    while kiri<(a-(b-1)):
        string=string+"*"
        kiri=kiri+1
    kanan=1
    while kanan<kiri -1:
        string=string+"*"
        kanan=kanan+1
    string=string+"\n"
    b=b-1
b=1
while b<=a:
    c=b+1
    while c>1:
        string=string+" "
        c=c-1
    kiri=0
    while kiri<(a-b):
        string=string+"*"
        kiri=kiri+1
    kanan=kiri
    while kanan>1:
        string=string+"*"
        kanan=kanan-1
    string=string+"\n"
    b=b+1
print(string)