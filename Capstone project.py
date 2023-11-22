#  Halaman Log in User
def login () :
    while True :
        username = input('''
            _______________________________________________

                  Selamat Datang di Crayon Open Library                  
            _______________________________________________
               
                        Username : ''')
        
        if (username == "Admin01"):
            password = int(input("\t\t\tPassword : "))
            if (password == 102218):
                mainMenu ()
            else :    
                print("\n\t\t Password yang Anda masukan Salah")
        else: 
            print("\n\t\tUsername yang Anda masukan salah")

# Data Peminjaman Buku
daftarPinjamBuku = [
    {
        'NPM'  : '18080299',
        'Nama' : 'Mahendra Prima',
        'Judul Buku' : 'Pengantar Bisnis',
        'Tanggal Peminjaman' : '02/08/2023',
        'Status' : 'Dikembalikan'
    },
    {
        'NPM'  : '18020196',
        'Nama' : 'Nabila Azizah',
        'Judul Buku' : 'Manajemen Bisnis',
        'Tanggal Peminjaman' : '12/07/2023',
        'Status' : 'Dikembalikan'
    },
    {
        'NPM'  : '18120193',
        'Nama' : 'Alyssa Permata',
        'Judul Buku' : 'Perilaku Organisasi',
        'Tanggal Peminjaman' : '25/06/2023',
        'Status' : 'Dikembalikan'
    },
    {
        'NPM'  : '18060006',
        'Nama' : 'Haikal Adimas',
        'Judul Buku' : 'Manajemen Keuangan',
        'Tanggal Peminjaman' : '20/10/2023',
        'Status' : 'Dipinjam'
    },
    {
        'NPM'  : '18080118',
        'Nama' : 'Azizah Famela',
        'Judul Buku' : 'Komunikasi Bisnis',
        'Tanggal Peminjaman' : '18/11/2023',
        'Status' : 'Dipinjam'
    }
]

# Main Menu 
def mainMenu () :
    while True :
       print('''
                         
                 _______________________________________
                |              Menu Utama               |
      
                             
                        1. Daftar Peminjaman Buku
                        2. Menambahkan Data Peminjaman Buku
                        3. Mengubah Data Peminjaman Buku
                        4. Menghapus Data Peminjaman Buku 
                        5. Pengembalian Peminjaman Buku  
                        6. Keluar           
                      
             ''')
       menu = input ('\n\t\t Masukan Pilihan Anda : ')
       if menu == '1' :
            daftarPeminjam()
       elif menu == '2' :
           menambahkanData()
       elif menu == '3' :
           mengubahData()
       elif menu == '4' :
           menghapusData()
       elif menu == '5' :
           pengembalianBuku()
       elif menu == '6' :
           keluar()
       else : 
           print("\n\t\t Pilihan Anda tidak ada. Silahkan masukkan Angka yang benar")
       

#  Menu 1 - DAFTAR PEMINJAMAN BUKU
def tampilkanData() :
    print('NPM\t\t | Nama \t\t | Judul Buku\t\t | Tanggal Peminjaman\t | Status\t |')
    for i in range(len(daftarPinjamBuku)):
        print('{}\t | {}\t | {}\t | {}\t\t | {}\t |'.format(daftarPinjamBuku[i]['NPM'],daftarPinjamBuku[i]['Nama'],daftarPinjamBuku[i]['Judul Buku'],daftarPinjamBuku[i]['Tanggal Peminjaman'],daftarPinjamBuku[i]['Status']))
    
   
def daftarPeminjam ():
    while True :
        menu1 = input('''
                         
 ___________________________________________________________________________________________
|                                   Daftar Peminjaman Buku                                  |


                        1. Tampilkan Seluruh Data Peminjam
                        2. Pencarian Berdasarkan NPM
                        3. Kembali ke Menu Utama
                      \n\t\t Masukan Pilihan Anda :''')
            
        if (menu1 == '1') :
            if len (daftarPinjamBuku) != 0 :
                tampilkanData()
                daftarPeminjam()
            else :
                print("\n\t\t Pilihan Anda tidak ada. Silahkan masukkan Angka yang benar")
                daftarPeminjam ()
        elif (menu1 == '2'): 
            if len(daftarPinjamBuku) != 0:
                npm = input("\n\t\t Silahkan masukkan data NPM yang dicari : ")
                for i in range(len(daftarPinjamBuku)):
                    if npm == daftarPinjamBuku[i]['NPM']:
                        print('NPM\t\t | Nama \t\t | Judul Buku\t\t | Tanggal Peminjaman\t | Status\t |')
                        print('{}\t | {}\t | {}\t | {}\t\t | {}\t |'.format(daftarPinjamBuku[i]['NPM'],daftarPinjamBuku[i]['Nama'],daftarPinjamBuku[i]['Judul Buku'],daftarPinjamBuku[i]['Tanggal Peminjaman'],daftarPinjamBuku[i]['Status']))
                        daftarPeminjam()
                else:
                    print ('\n\t\t Data yang Anda cari tidak ada')
                    daftarPeminjam()
            else:
                print ('\n\t\t Data yang Anda cari tidak ada')
                daftarPeminjam()
        elif (menu1 == '3'):
            mainMenu()
        else :
                print ("\n\t\t Pilihan yang Anda Masukkan tidak ada")
                daftarPeminjam()
        

#  Menu 2 - MENAMBAHKAN DATA PEMINJAMAN 
def menambahkanData() :
    while True :
        menu2 = input('''
 _____________________________________________________________________________________________
|                              Menambahkan Data Peminjaman Buku                               |
                      
                1 - Menambahkan Peminjaman Buku
                2 - Kembali ke main menu

        Masukan pilihan menu yang ingin dijalankan:  ''')

        if (menu2 == '1') :
            while True :
                npm = input('\n\n\t Masukan NPM yang ingin dipinjam :')
                for i in range(len(daftarPinjamBuku)) :
                    if daftarPinjamBuku[i]['NPM'] == npm :
                        print ("\n\t\t Tidak ada data yang tersedia")
                        break
                else :
                    namaPeminjam = input('\t\t Masukan nama peminjam buku : ')
                    judulBuku = (input('\t\t Masukan Judul Buku yang dipinjam buku : '))
                    tglPeminjam = input('\t\t Masukan tanggal peminjaman buku : ')
                    statusPeminjam = input('\t\t Masukan status buku :')
                    while True :
                        checker = input('\n\t\t Apakah data yang Anda masukan sudah benar? ya/tidak : ')
                        if checker == 'ya' :
                            daftarPinjamBuku.append ({
                            'NPM' : npm,
                            'Nama' : namaPeminjam,
                            'Judul Buku' : judulBuku,
                            'Tanggal Peminjaman' : tglPeminjam,
                            'Status' : statusPeminjam,        
                            })
                            tampilkanData()
                            print ('\n\t\t Data yang Anda masukkan telah tersimpan, silahkan cek kembali')
                            break
                        elif checker == 'tidak' :
                            tampilkanData()
                            print ('\n\t\t Data yang Anda masukkan tidak tersimpan, silahkan masukkan ulang')
                            break
                        else :
                            print('\n\t\t Jawaban yang Anda masukkan salah, silahkan pilih antara ya/tidak')
                break            
        elif (menu2 == '2') :
            break
        else :
            print("\n\t\t Pilihan yang Anda Masukkan tidak ada")

# Mengubah Data Peminjaman Buku
def mengubahData():
    while True:
        menu3 = input ('''
 ________________________________________________________________________________________
|                              Mengubah Data Peminjaman Buku                             |
                      
                1 - Mengubah Data Peminjaman Buku
                2 - Kembali ke main menu

            \n\t\t Masukan pilihan menu yang ingin dijalankan:  ''')
        if menu3 == '1':
            ubahnpm = input('\n Masukkan NPM data peminjam yang ingin diubah : ')
            for i in range(len(daftarPinjamBuku)):
                if ubahnpm == daftarPinjamBuku[i]['NPM']:
                    print ('NPM\t\t | Nama \t\t | Judul Buku\t\t | Tanggal Peminjaman\t | Status \t |')
                    print('{}\t | {}\t | {}\t\t | {}\t | {}\t |'.format(daftarPinjamBuku[i]['NPM'],daftarPinjamBuku[i]['Nama'],daftarPinjamBuku[i]['Judul Buku'],daftarPinjamBuku[i]['Tanggal Peminjaman'],daftarPinjamBuku[i]['Status']))
                    ubahData = input ("\n\t\t Apakah benar data ini yang ingin diubah? ya/tidak : ")
                    if ubahData =='ya':
                        ubahKategori = input('\n Apa yang Anda ingin ubah? : ')
                        if ubahKategori == 'Nama':
                            ubahNama = input('\n\t\t Silahkan Masukkan Nama yang benar : ')
                            update = input('\n\t\t Apakah Anda yakin ingin mengubah data ini? ya/tidak : ')
                            if update == 'ya':
                                daftarPinjamBuku[i][ubahKategori] = ubahNama
                                print ("\n\t\t Data tersebut berhasil diubah, silahkan cek kembali")
                                mengubahData()
                            else:
                                print("\n\t\t Data yang Anda masukkan tidak tersimpan, silahkan masukkan ulang")
                                mengubahData()
                        elif ubahKategori == 'Judul Buku':
                            ubahJudulBuku = input('\n\t\t Silahkan Masukkan Judul Buku yang benar')
                            update = input('\n\t\t Apakah Anda yakin ingin mengubah data ini? ya/tidak : ')
                            if update == 'ya':
                                daftarPinjamBuku[i][ubahKategori] = ubahJudulBuku
                                print ("\n\t\t Data tersebut berhasil diubah, silahkan cek kembali")
                                mengubahData()
                            else:
                                print("\n\t\t Data yang Anda masukkan tidak tersimpan, silahkan masukkan ulang")
                                mengubahData()
                        elif ubahKategori == 'Tanggal Peminjaman':
                            ubahTglPinjam =  input('\n\t\t Silahkan Masukkan Tanggal Peminjaman yang benar')
                            update = input('\n\t\t Apakah Anda yakin ingin mengubah data ini? ya/tidak : ')
                            if update == 'ya':
                                daftarPinjamBuku[i][ubahKategori] = ubahTglPinjam
                                print ("\n\t\t Data tersebut berhasil diubah, silahkan cek kembali")
                                mengubahData()
                            else:
                                print("\n\t\t Data yang Anda masukkan tidak tersimpan, silahkan masukkan ulang")
                                mengubahData()
                        elif ubahKategori == 'Status':
                            ubahStatus =  input('\n\t\t Silahkan Masukkan Status yang benar : ')
                            update = input('\n\t\t Apakah Anda yakin ingin mengubah data ini? ya/tidak : ')
                            if update == 'ya':
                                daftarPinjamBuku[i][ubahKategori] = ubahStatus
                                print ("\n\t\t Data tersebut berhasil diubah, silahkan cek kembali")
                                mengubahData()
                            else:
                                print("\n\t\t Data yang Anda masukkan tidak tersimpan, silahkan masukkan ulang")
                                mengubahData()
                        else:
                            mengubahData()
                    else:
                        mengubahData()
            else:
                print("\n\t\t Pilihan yang Anda Masukkan tidak ada")
                mengubahData()
        elif menu3 == '2':
            mainMenu()
        else:
            print("\n\t\t Pilihan yang Anda Masukkan tidak ada")
            mengubahData()

# Menghapus Data
def menghapusData() :
    while True:
        menu4 = input ('''
 ________________________________________________________________________________________
|                              Menghapus Data Peminjaman Buku                             |
                      
                1 - Menghapus Data Peminjaman Buku
                2 - Kembali ke main menu

            "\n\t\t Masukan pilihan menu yang ingin dijalankan:  ''')
        if menu4 == '1' :
            npm = input ('\n\t\t Masukan NPM yang ingin dihapus : ')
            for i in range(len(daftarPinjamBuku)):
                if npm == daftarPinjamBuku[i]['NPM']:
                    update = input('\n\t\t Apakah Anda yakin ingin mengubah data ini? ya/tidak : ')
                    if update =='ya':
                        del daftarPinjamBuku[i]
                        print ("\n\t\t Data peminjaman buku yang Anda pilih telah dihapus")
                        menghapusData()
                    else:
                        print ("\n\t\t Data yang Anda pilih tidak terhapus, silahkan coba kembali")
                        menghapusData()
        elif menu4 == '2':
            mainMenu()
        else:
            print("\n\t\t Pilihan yang Anda Masukkan tidak ada")
            menghapusData()

# Pengembalian Buku 
def pengembalianBuku (): 
    while True :
        menu5 = input ('''
 ___________________________________________________________________________
|                              Pengembalian Buku                            |
                      
                1 - Pengembalian Buku
                2 - Kembali ke main menu

            "\n\t\t Masukan pilihan menu yang ingin dijalankan:  ''')
        if menu5 == '1':
            npm = input('\n Masukkan NPM data peminjam yang ingin mengembalikan : ')
            for i in range(len(daftarPinjamBuku)):
                if npm == daftarPinjamBuku[i]['NPM']:
                    print ('NPM\t\t | Nama \t\t | Judul Buku\t\t | Tanggal Peminjaman\t | Status \t |')
                    print('{}\t | {}\t | {}\t\t | {}\t | {}\t |'.format(daftarPinjamBuku[i]['NPM'],daftarPinjamBuku[i]['Nama'],daftarPinjamBuku[i]['Judul Buku'],daftarPinjamBuku[i]['Tanggal Peminjaman'],daftarPinjamBuku[i]['Status']))
                    kembalikanBuku = input ("\n\t\t Apakah Anda yakin ingin mengembalikan buku? ya/tidak : ")
                    if kembalikanBuku =='ya':
                        ubahStatus =  input('\n\t\t Silahkan updata status peminjaman : ')
                        update = input('\n\t\t Apakah Anda yakin ingin mengubah data ini? ya/tidak : ')
                        if update == 'ya':
                            daftarPinjamBuku[i][kembalikanBuku] = ubahStatus
                            print ("\n\t\t Buku telah berhasil dikembalikan, silahkan cek kembali")
                            mengubahData()
            else:
                print("\n\t\t Pilihan yang Anda Masukkan tidak ada")
                mengubahData()
        elif (menu5 == '2') :
            mainMenu()
        else :
            print("\n\t\t Pilihan yang Anda Masukkan tidak ada")


# Keluar 
def keluar():
    print('\n\t\t --------------Terima kasih telah menggunakan Crayon Open Library--------------')
    exit()

login ()