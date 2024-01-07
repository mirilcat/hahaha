import mysql.connector

db = mysql.connector.connect(
    hodt="localhost",
    user="root",
    passwd=""
)



nim = input("masukan NIM anda          : ")
nama = input("masukkan NAMA anda        : ")
kelas = input("masukkan KELAS anda       : ")
 
print("###################################################################################")


listpilihan=[]
listjb=[]
listharga=[]
listjenis=[]
listtotbel=[]
listket=[]
totbelanja=0
totsemua=0

def garis() :
    print("###############################################################################")
    
print("=> TOKO CAT MI <=".center(90))
print("JL. BOJONG GEDE".center(90))
print("KEC. ILIR BARAT II prov. Jawa Barat".center(90))
print("contact person : 082239998333".center(90))

garis()
print("PROMO DISKON 10% SETIAP BELANJA MINIMAL 100K".center(90))
print("FOLLOW OUR INSTAGRAM FOR MORE PROMO".center(90))
garis()
n_petugas=input("masukkan nama petugas : ")
n_kode=input("masukkan kode petugas : ")
n_pembeli=input("masukkan nama pembeli : ")

garis()
print("jenis Cat Yang Tersedia : ")
print("1. Dinding                         ")
print("2. Pagar                           ")
print("3. Kayu                            ")
print("4. Besi                            ")
print("5. Waterproofing                   ")
print("6. Marine Coating                  ")
print("7. Akrilik                         ")
print("8. Gouache                         ")
garis()


a=int(input("Berapa total Jenis cat yang anda inginkan : "))

for i in range(a):
    print(" Jenis Cat ke- ",i+1)
    pilihan=int(input("pilihan [1/2/3/4/5/6/7/8] : "))
    listpilihan.append(pilihan)
    jb=int(input("jumlah beli : "))
    listjb.append(jb)

    if (listpilihan[i]==1):
        listjenis.append("Dinding                   ")
        listharga.append(50000)
    elif (listpilihan[i]==2):
        listjenis.append("Pagar                     ")
        listharga.append(55000) 
    elif (listpilihan[i]==3):
        listjenis.append("Kayu                      ")
        listharga.append(42000)
    elif (listpilihan[i]==4):
        listjenis.append("Besi                      ")
        listharga.append(30000)
    elif (listpilihan[i]==5):
        listjenis.append("Waterproofing             ")
        listharga.append(78000)
    elif (listpilihan[i]==6):
        listjenis.append("Marine Coating            ")
        listharga.append(120000)
    elif (listpilihan[i]==7):
        listjenis.append("Akrilik                   ")
        listharga.append(25000)
    elif (listpilihan[i]==8):
        listjenis.append("Gouache                   ")
        listharga.append(45000)
    else : 
        listpilihan = ("Tidak Ada")

    listtotbel.append(listjb[i]*listharga[i])

    if listjb [i>9] :
        listket.append("Ada")
    else :
        lisket.append("Tidak Ada")
        
print("=> TOKO CAT MI <=".center(90))

print("###############################################################################")

print("nama petugas          : ", n_petugas)
print("Kepada Yth, Bpk/Ibu   : ", n_pembeli,", berikut adalah Rincian Pembelian Anda")
print("===============================================================================")
print("| no.|     Jenis     | harga |  jumlah  | total |   Ket  |")  
print("_______________________________________________________________________________")

for i in range(a):
    print("| %d. | %s | Rp.%d  |   %d   |  Rp.%d  | %s |"  %(i+1, listjenis[i], listharga[i], listjb[i], listtotbel[i], listket[i]))
    totbelanja=totbelanja+listjb[i]
    totsemua=totsemua+listtotbel[i]
print("______________________________________________________________________________")
print("total belanja                    = ", totbelanja, "(item)")
print("total harga semuanya             = Rp. ", totsemua)
diskon = totsemua - 0.10 * totsemua
totdiskon = totsemua - diskon
if (totsemua >= 100000):
    print("Total Diskon 10%                 = Rp. ", totdiskon)
    print("Harga bayar menjadi              = Rp. ", diskon)
else :
    print("Total Diskon 0%                  = Rp. 0 ")
    print("Harga bayar menjadi              = Rp.", totsemua)
    
print("===============================================================================")

bayar=int(input("masukkan jumlah yang dibayar\t   = "))   
kembali1 = bayar - diskon
kembali = bayar - totsemua
if (totsemua >= 100000) :
    print("Uang kembali anda                 = Rp. ", kembali1)
else :
    print("Uang kembali anda                  = Rp. ", kembali2)

print("===============================================================================")
print("Terima Kasih Sudah Berbelanja! :) ")

garis()
print("NIM      : ", nim)
print("NAMA     : ", nama)
print("KELAS    : ", kelas)

garis()
