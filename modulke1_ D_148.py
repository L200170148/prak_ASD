print('Nomer 1')
def cetakSiku():
    for i in range(5):
     for j in range(i+1):
        print('*', end='')
     print()
cetakSiku()
print('\nNomer 2')
def gambarlahPersegiPanjang(tinggi,lebar):
    for i in range(tinggi):
        if i==0 or i==tinggi-1:
                print ('@'*lebar)
        else:
            print ('@'+' '*(lebar-2)+'@')
        
gambarlahPersegiPanjang(4,5)
print('\nNomer 3a')
def itung(x):
    vokal='aiueoAIUEO'
    a=0
    for i in x:
        if i in vokal:
            a+=1
    return(len(x), a)
print (itung('Surakarta'))
print('\nNomer 3b')
def itung(x):
    konsonan='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    a=0
    for i in x:
        if i in konsonan:
            a+=1
    return(len(x), a)
print (itung('Surakarta'))
print('\nNomer 4')
def rerata(p=[]):
    x=0
    n=0
    if p != []:
        for i in p:
            x+=i
            n+=1
        return x/n
z=rerata([1,2,3,4,5])
print(z)

g=[3,4,5,4,3,4,5,2,2,10,11,23]
r=rerata(g)
print(r)
print("\nNomer 5")
from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primakecil=[2, 3, 5, 7, 11]
    bukanprima=[0, 1, 4, 6, 8, 9, 10]
    if n in primakecil:
        return True
    elif n in bukanprima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True
print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))
print("\nNomer 6")
def bilanganprima():
    prima=list()
    for i in range(2,100):
        x = True
        for iter in prima:
            if(i%iter==0):
                x=False
                break
        if(x):
            print(i)
            prima.append(i)
bilanganprima()
print("\nNomer 7")
def faktorPrima(n):
    prima=list()
    for i in range(2,n):
        x = True
        for iter in prima:
            if(i%iter==0):
                x=False
                break
        if x and n%i==0:
            prima.append(i)
    return prima
print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))
print("\nNomer 8")
def apakahTerkandung(a,b):
    return a in b
h ="do"
k ="Indonesia tanah air kita"
print(apakahTerkandung(h,k))
print(apakahTerkandung("pusaka",k))
print("\nNomer 9")
def ahay():
    for a in range(1,100):
        if (a%3)!=0 and (a%5)!=0:
            print(a)
        else:
            if (a%15)==0:
                print("PYTHON UMS")
            elif (a%3)==0:
                print("python")
            elif (a%5)==0:
                print("UMS")
ahay()
print("\nNomer 10")
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    d=(b**2)-(4*a*c)
    if d<0:
        return "determinan negatif. Persamaan tidak mempunyai akar real"
    return  "determinanpositif. Persamaan mempunyai akar real"
print(selesaikanABC(1,2,3))
print("\nNomer 11")
def apakahkabisat(x):
    if(x%400==0):
        return True
    if(x%100==0):
        return False
    if(x%4==0):
        return True
    return False
print(apakahkabisat(2400))
print("\nNomer 12")
import random
def permainanTA():
    a=random.randrange(0, 100)
    while(True):
        c=int(input("masukan angka: "))
        if(c>a):
            print("itu terlalu besar,coba lagi")
        elif(c<a):
            print("itu terlalu kecil,coba lagi")
        else:
            print("benar")
            break
permainanTA()
print("\nNomer 13")
def katakan(z):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",-6:"ratus ",-7:"juta ",8:"puluhjuta "}
    d=str(z)
    z=""
    i=-1
    while i>= -len(d):
        z=x[d[i]]+y[i]+z
        i-=1
    return z
print(katakan(3125750))
print("\nNomer 14")
def formatRupiah(x):
    y=str(x)
    z=""
    i = -1
    while i>= -len(y):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+z
        z=y[i]+z
        i-=1
    return "'"+"Rp "+z+"'"
print(formatRupiah(1500))
print(formatRupiah(2560000))
             



