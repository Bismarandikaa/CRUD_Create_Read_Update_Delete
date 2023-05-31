#Capstone Project Modul 1
#Nama: Bisma Randika Wijaksana

#Dictionary di dalam List
nilaiSiswa = [
    {
        'Npm': 100,
        'Nama': 'Andhika',
        'Jenis Kelamin': 'L',
        'Nilai': 80,
        'Keterangan': 'Lulus'
    },
    {
        'Npm': 101,
        'Nama': 'Budi',
        'Jenis Kelamin': 'L',
        'Nilai': 50,
        'Keterangan': 'Tidak Lulus'
    },
    {
        'Npm': 102,
        'Nama': 'Putri',
        'Jenis Kelamin': 'P',
        'Nilai': 90,
        'Keterangan': 'Lulus'    
    }
]

#Menampilkan seluruh data nilai siswa
def DaftarNilaiSiswa():
    print('''
                    = = = = = = Daftar Nilai Siswa = = = = = = 
                        = = = SMA Purwadhika Jakarta = = =\n''')
    
    print('''No \t| Npm \t| Nama  \t| Jenis Kelamin \t| Nilai \t| Keterangan''') 
    for i in range(len(nilaiSiswa)):
        print('{} \t| {} \t| {}   \t| {} \t\t\t| {} \t\t| {}'.format(i+1,nilaiSiswa[i]['Npm'],nilaiSiswa[i]['Nama'],nilaiSiswa[i]['Jenis Kelamin'],nilaiSiswa[i]['Nilai'],nilaiSiswa[i]['Keterangan']))

#READ - Menu 1 nilai data siswa 
def MenuNilaiSiswa():
    while True:
        print('''
        =========== Menu Data Nilai Siswa ==========
        
        1. Tampilkan keseluruhan nilai data siswa
        2. Tampilkan data tertentu
        3. Exit ke Menu Utama\n''')

        SubMenu = int(input('''Silahkan pilih menu [1 - 3 ] di atas : '''))
        if SubMenu == 1:
            DaftarNilaiSiswa()
        elif SubMenu == 2:
            DataTertentu()
        elif SubMenu == 3:
            Menu_Utama()
        else :
            print('Menu yang anda pilih tidak tersedia\nMohon menggunakan menu yang ada: ')
            continue

#Tampilkan nilai data tertentu siswa. SubMenu 1
def DataTertentu():
    DaftarNilaiSiswa()
    inputNpm = int(input('''
        Masukan Npm siswa: '''))
    for i in range (len(nilaiSiswa)):
        if inputNpm == nilaiSiswa[i]['Npm']:
            print(f'''\n\t\t=== Data nilai siswa ditemukan ===\n
     === Siswa dengan Npm: {inputNpm} memiliki data sebagai berikut ===\n
            === Data nilai siswa SMA Purwadhika Jakarta ===\n''')
            print('No. \t|Npm \t| Nama   \t| Jenis Kelamin \t| Nilai \t| Keterangan')
            print('{} \t| {} \t| {}   \t| {} \t\t\t| {} \t\t| {}'.format(i+1,nilaiSiswa[i]['Npm'],nilaiSiswa[i]['Nama'],nilaiSiswa[i]['Jenis Kelamin'],nilaiSiswa[i]['Nilai'],nilaiSiswa[i]['Keterangan']))
            break
        elif (i == len(nilaiSiswa)-1) and (inputNpm != nilaiSiswa[i]['Npm']):
            print('''\n\t\t=== Data siswa tidak ditemukan ===''')
            continue

#CREATE - Menu 2 menambahkan nilai data siswa
def AddData():
    while True:
        TambahDataSiswa = input('''
        ======= Menu Menambah Data Nilai Siswa =======
        
                1. Tambahkan data nilai siswa
                2. Exit ke menu utama

Silahkan pilih menu [1 - 2] tambah data di atas : ''')

        if TambahDataSiswa == '1':
            DaftarNilaiSiswa()
            NpmSiswa = int(input('\nMasukan Npm baru : '))
            for i in range(len(nilaiSiswa)):
                if NpmSiswa == nilaiSiswa [i]['Npm']:
                    print('''
                === Nilai siswa dengan Npm ini sudah ada di dalam database ===
                === Mohon input Npm baru === ''')
                    AddData()
                elif (i == len(nilaiSiswa)-1) and NpmSiswa != nilaiSiswa[i]['Npm'] :
                    NamaSiswa = input('Nama :').capitalize()
                    JenisKelamin = input('Jenis Kelamin :').capitalize()
                    Nilai = int(input('Nilai :'))
                    Keterangan = input('Keterangan :').capitalize()   
            Konfirmasi = input('''
                === Apakah data ingin ditambahkan (Y/T)?: ''').capitalize()
            if Konfirmasi == 'Y':
                nilaiSiswa.append({
                    'Npm': NpmSiswa,
                    'Nama': NamaSiswa,
                    'Jenis Kelamin': JenisKelamin,
                    'Nilai': Nilai,
                    'Keterangan': Keterangan
                })
                print('\n=== Data nilai siswa sudah berhasil ditambahkan ===')
                DaftarNilaiSiswa()
                AddData()

            elif Konfirmasi == 'T':
                print('\n=== Data nilai siswa tidak jadi ditambahkan ===')
                AddData()
            else :
                    print('''\n=== Pilihan yang anda masukan salah ===
                === Silahkan masukan kembali pilihan yang benar (Y/T):''')
                    continue
        elif TambahDataSiswa == '2':
            Menu_Utama()
        else:
            print('''
    === Pilihan yang anda masukan salah ===
    === Silahkan masukan kembali pilihan yang benar (1-2):''')
            continue

#UPDATE - Menu ke 3 mengubah data nilai siswa
def UpdateData():
    while True:
        UpdateDataSiswa = input('''
        ==== Menu Update Data Siswa ====
            1. Update data siswa
            2. Kembali ke menu utama

            Silahkan pilih menu di atas [1-2] :''')

        if UpdateDataSiswa == '1':
            DaftarNilaiSiswa()
            NpmSiswa = (int(input('\n\t=== Masukan Npm siswa: ')))
            for i in range(len(nilaiSiswa)):
                if NpmSiswa == nilaiSiswa[i]['Npm'] :
                    while True:
                        print('''
                        === Data siswa ditemukan ===\n''')
                        print('''No.\t| Npm \t| Nama \t\t| Jenis Kelamin \t| Nilai \t| Keterangan''')
                        print('{} \t| {} \t| {}   \t| {} \t\t\t| {} \t\t| {}'.format(i+1,nilaiSiswa[i]['Npm'],nilaiSiswa[i]['Nama'],nilaiSiswa[i]['Jenis Kelamin'],nilaiSiswa[i]['Nilai'],nilaiSiswa[i]['Keterangan']))
                        Konfirmasi = input('''
                        === Apakah anda ingin mengubah data (Y/T)?: ''').capitalize()
                        if Konfirmasi == 'Y' :
                            ubah_kolom = input('pilih kolom yang ingin diubah (Npm, Nama, Jenis Kelamin, Nilai, Keterangan): ').lower()
                            if ubah_kolom == nilaiSiswa[i]['Npm'] :
                                ubah_kolom = ubah_kolom.upper()
                            else:
                                ubah_kolom = ubah_kolom.capitalize()
                            ubah_isi = input(f'Masukan {ubah_kolom} baru : ').capitalize()
                            while True:
                                Konfirmasi1 = input('Apakah data ingin diubah(Y/T)?: ').capitalize()
                                if Konfirmasi1 == 'Y':
                                    nilaiSiswa[i][ubah_kolom] = ubah_isi
                                    print('''
                                \n\t\t=== Data sudah berhasil diubah ===''')
                                    DaftarNilaiSiswa()
                                    UpdateData()
                                elif Konfirmasi1 == 'T' :
                                    print('\n=== Data nilai siswa tidak jadi diubah ===')
                                    UpdateData()
                                else:
                                    print('Mohon masukan (Y/T) saja')
                                    continue
                elif (i == len(nilaiSiswa)-1) and (NpmSiswa != nilaiSiswa[i]['Npm']) :
                    print('''
                    === Data nilai siswa tidak ditemukan ===''')
        elif UpdateDataSiswa == '2':
            Menu_Utama()
        else:
            print('''
    === Pilihan yang anda masukan salah ===
    === Silahkan masukan kembali pilihan yang benar (1-2):''')
            continue

#DELETE - Menu ke 4 hapus data siswa
def DeleteData():
    DaftarNilaiSiswa()
    while True:
        DeleteDataSiswa = input('''
    === Menu Menghapus Data Nilai Siswa === 
            1. Hapus data nilai siswa
            2. Kembali ke menu utama
        
    Silahkan pilih menu di atas [1-2] : ''')
        if DeleteDataSiswa == '1':
            NpmSiswa = int(input('''
    Masukan Npm siswa yang akan dihapus data nilainya: '''))
            for i in range(len(nilaiSiswa)):
                if NpmSiswa == nilaiSiswa[i]['Npm']:
                    while True :
                        print('''
                === Data siswa telah ditemukan ===\n''')
                        print('No. \t|Npm \t| Nama   \t| Jenis Kelamin \t| Nilai \t| Keterangan')
                        print('{} \t| {} \t| {}   \t| {} \t\t\t| {} \t\t| {}'.format(i+1,nilaiSiswa[i]['Npm'],nilaiSiswa[i]['Nama'],nilaiSiswa[i]['Jenis Kelamin'],nilaiSiswa[i]['Nilai'],nilaiSiswa[i]['Keterangan']))
                        while True:
                            Konfirmasi = input('''
    === Apakah anda yakin untuk menghapus nilai data dari siswa ini (Y/T)?: ''').capitalize()
                            if Konfirmasi == 'Y':
                                del nilaiSiswa[i]
                                print(f'''
    === Data siswa dengan Npm : {NpmSiswa} berhasil dihapus ===''')
                                DeleteData()
                            elif Konfirmasi == 'T':
                                print('''
    === Data siswa tidak jadi dihapus ===''')
                                DeleteData()
                            else:
                                print('''
    === Pilihan yang anda masukan salah === 
    Silahkan masukan kembali pilihan yang benar (Y/T): ''')
                                continue
            else:
                print('''
    === Npm yang ada masukan salah ===
    === Mohon menggunakan Npm yang tersedia ===''')
                DeleteData()

        elif DeleteDataSiswa == '2':
            Menu_Utama()
        else:
            print('''
    === Pilihan yang anda masukan salah ===
    === Silahkan masukan kembali pilihan yang benar (1-2):''')
            continue

#Menu Utama
def Menu_Utama():
    print('''
= = = = = Halo! Selamat datang di SMA Purwadhika Jakarta = = = = =

        = = = = = = = = Daftar Menu = = = = = = = = 
            
            1. Data Nilai Siswa
            2. Menambahkan Data Nilai Siswa
            3. Mengubah Data Nilai Siswa
            4. Menghapus Data Nilai Siswa
            5. Keluar ''') 

    while True:
        OpsiMenu = input('\nSilahkan pilih nomor di atas (1-5): ')      
        if OpsiMenu == '1':
            MenuNilaiSiswa()
        elif OpsiMenu == '2':
            AddData()
        elif OpsiMenu == '3':
            UpdateData()
        elif OpsiMenu == '4':
            DeleteData()
        elif OpsiMenu == '5':
            print('\n=== Terima kasih telah menggunakan layanan ini, sampai jumpa! ===\n')
            exit()
        else:
            print('Anda memasukan pilihan yang salah\nSilahkan masukan pilihan yang benar (1-5) ')
Menu_Utama()