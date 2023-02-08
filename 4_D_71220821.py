print("--------Nilai Ke 1--------")
def nilai()
    a=int(input("Nilai Harian :"))
    b=int(input("Nilai UTS :"))
    c=int(input("Nilai UAS :"))
    d=a*0.3+b*0.3+c*0.4
nilai()
print("--------Nilai Ke 2--------")
nilai()
print("--------Total Nilai--------")

hasil=d/2
print("Total nilai yang didapat :", hasil)
if hasil>=0 and hasil<=19:
    print("Total Nilai Dalam Huruf : E")
elif hasil>=20 and hasil<=39:
    print("Total Nilai Dalam Huruf : D")
elif hasil>=40 and hasil<=59:
    print("Total Nilai Dalam Huruf : C")
elif hasil>=60 and hasil<=79:
    print("Total Nilai Dalam Huruf : B")
elif hasil>=80 and hasil<=100:
    print("Total Nilai Dalam Huruf : A")