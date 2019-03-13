print ("No 1")
class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakKapital(self):
        print(str.upper(self.teks))
    def cetakKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlah(self):
        print("Kalimatku mempunyai: ",len(self.teks),"karakter")
    def perbarui(self, strBaru):
        self.teks = strBaru

    def apaTerkandung(self, isi):
        if str(isi) in self.teks:
            print("true")
        else:
            print("false")
    def hitungV(self):
        v = "aiueoAIUEO"
        n = 0
        for i in self.teks:
            if i in v:
                n+=1
        return n

    def hitungK(self):
        v = "aiueoAIUEO"
        n = 0
        for i in self.teks:
            if i not in v:
                n+=1
        return n

kataku = Pesan("Indonesia adalah negeri yang indah")
kataku.apaTerkandung("ege")
kataku.apaTerkandung("eka")
print(kataku.hitungV())
print(kataku.hitungK())

print ("\nNo 2")
class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama+", NIM"+str(self.NIM)\
            +". Tinggal di" +self.kotaTinggal \
            +". Uang saku Rp."+str(self.uangsaku)\
            +" tiap bulan."
        return s
    def ambilNama(self):
        print (self.nama)
    def ambilNIM(self):
        print (self.NIM)
    def ambilUangSaku(self):
        print (self.uangsaku)
    def makan(self,s):
        """Metode ini menutupi makan -nya class Manusia. Mahasiswa kalau makan sambil belajar"""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan="Kenyang"
        
    def ambilKotaTinggal(self):
        print (self.kotaTinggal)
        
    def perbaruiKotaTinggal(self, baru):
        self.kotaTinggal = baru
        
    def tambahUangSaku(self, uang):
        self.uangsaku = self.uangsaku + uang

mhs1 = Mahasiswa("Wayang",420,'Surabaya',270000)
print (mhs1.ambilKotaTinggal())
mhs1.perbaruiKotaTinggal('Sleman')
print (mhs1.ambilKotaTinggal())
print (mhs1.ambilUangSaku())
mhs1.tambahUangSaku(50000)
print (mhs1.ambilUangSaku())

print ("\nNo 3")
nama = input("Masukkan Nama Anda : ")
nim = input("Masukkan NIM Anda : ")
kt = input("Masukkan Kota Tinggal Anda : ")
us = input("Masukkan Uang Saku Anda : ")
mhs2 = Mahasiswa(nama,nim,kt,us)
mhs2.ambilNama()
mhs2.ambilNIM()
mhs2.ambilKotaTinggal()
mhs2.ambilUangSaku()

print ("\nNo 4")
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    matkul=[]
    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama+", NIM"+str(self.NIM)\
            +". Tinggal di" +self.kotaTinggal \
            +". Uang saku Rp."+str(self.uangsaku)\
            +" tiap bulan."
        return s
    def ambilNama(self):
        print (self.nama)
    def ambilNIM(self):
        print (self.NIM)
    def ambilUangSaku(self):
        print (self.uangsaku)
    def makan(self,s):
        """Metode ini menutupi makan -nya class Manusia. Mahasiswa kalau makan sambil belajar"""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan="Kenyang"
        
    def ambilKotaTinggal(self):
        print (self.kotaTinggal)
        
    def perbaruiKotaTinggal(self, baru):
        self.kotaTinggal = baru
        
    def tambahUangSaku(self, uang):
        self.uangsaku = self.uangsaku + uang
    def ambilMK(self, mk):
        self.matkul.append(mk)
    def listKuliah(self):
        print(self.matkul)


mhs3 = Mahasiswa("rrr","r","rrr","rrrrr")
mhs3.ambilMK("Matematika Diskret")
mhs3.listKuliah()
mhs3.ambilMK("Algoritma Dan Struktur Data")
mhs3.listKuliah()

print ("\nNo 5")
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    matkul=[]
    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama+", NIM"+str(self.NIM)\
            +". Tinggal di" +self.kotaTinggal \
            +". Uang saku Rp."+str(self.uangsaku)\
            +" tiap bulan."
        return s
    def ambilNama(self):
        print (self.nama)
    def ambilNIM(self):
        print (self.NIM)
    def ambilUangSaku(self):
        print (self.uangsaku)
    def makan(self,s):
        """Metode ini menutupi makan -nya class Manusia. Mahasiswa kalau makan sambil belajar"""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan="Kenyang"
        
    def ambilKotaTinggal(self):
        print (self.kotaTinggal)
        
    def perbaruiKotaTinggal(self, baru):
        self.kotaTinggal = baru
        
    def tambahUangSaku(self, uang):
        self.uangsaku = self.uangsaku + uang
    def ambilMK(self, mk):
        self.matkul.append(mk)
    def listKuliah(self):
        print(self.matkul)
    def hapusKuliah(self, mk):
        return self.matkul.remove(mk)

mhs3 = Mahasiswa("rrr","r","rrr","rrrrr")
mhs3.ambilMK("Matematika Diskret")
mhs3.listKuliah()
mhs3.ambilMK("Algoritma Dan Struktur Data")
mhs3.listKuliah()
mhs3.hapusKuliah("Matematika Diskret")
mhs3.listKuliah()

print ("\nNo 6")
class SiswaSMA(Manusia):
    def __init__(self, nama, nisn, sma, hobi):
        self.nama = nama
        self.nisn = nisn
        self.sma = sma
        self.hobi= hobi
    def __str__(self):
        return "\n\nData Diri\n"\
               +"Nama   : "+self.nama\
               +"\nNISN   : "+str(self.nisn)\
               +"\nSMA    : "+self.sma\
               +"\nHobi   : "+self.hobi\
               
    def ambilNama(self):
        print (self.nama)
    def ambilNISN(self):
        print (self.nisn)
    def ambilSma(self):
        print (self.sma)
    def ambilHobi(self):
        print (self.hobi)

sma=SiswaSMA("Wayang","8984986785","Harapan Bangsa", "Sepak Bola")
print(sma)

print ("\nNo 7")
class MhsTIF(Mahasiswa):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanpy(self):
        print('Python is cool.')
