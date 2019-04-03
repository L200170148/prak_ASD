print('No 1')
class Mahasiswa(object):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        
def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp

        
c0 = Mahasiswa('Nene',10,'Sukoharjo',240000)
c1 = Mahasiswa('Bana',51,'Sragen',230000)
c2 = Mahasiswa('Abi',2,'Surakarta',250000)
c3 = Mahasiswa('Candra',18,'Surakarta',235000)
c4 = Mahasiswa('Eko',4,'Boyolali',240000)
c5 = Mahasiswa('Dandi',31,'Salatiga',250000)
c6 = Mahasiswa('Beni',13,'Klaten',245000)
c7 = Mahasiswa('Waluh',5,'Wonogiri',245000)
c8 = Mahasiswa('Joko',23,'Klaten',245000)
c9 = Mahasiswa('Him',64,'Karanganyar',270000)
c10 = Mahasiswa('Kedar',29,'Purwodadi',230000)

angka = [c0.NIM,c1.NIM,c2.NIM,c3.NIM,c4.NIM,c5.NIM,c6.NIM,c7.NIM,c8.NIM,c9.NIM,c10.NIM]
BubbleSort(angka)
print(angka)

print('\nNo 2')
def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp
 
angka = [23,7,32,99,4,15,11,20]
BubbleSort(angka)
a = angka
angka1 = [23,7,32,99,4,15,11,20]
BubbleSort(angka1)
b = angka1
angka2 = (a+b)
BubbleSort(angka2)
c = angka2
print(c)

print('\nNo 3')
from time import time as detak
from random import shuffle as kocok

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos -1]
            pos = pos -1
        A[pos] = nilai

def swap(A,p,q):
    tmp = A[p]
    A[p]= A[q]
    A[q]= tmp

def cariPosisiYangTerkecil(A,darisini, sampaisini):
    posisiYangTerkecil = darisini
    for i in range (darisini+1, sampaisini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

k = []
for i in range(1,6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak = detak();print('bubble: %g detik' %(ak-aw));
aw = detak();selectionSort(u_sel);ak = detak();print('selection: %g detik' %(ak-aw));
aw = detak();insertionSort(u_ins);ak = detak();print('insertion: %g detik' %(ak-aw));
