listAksesoris = [
    {
        'kode': 'A001',
        'jenis': 'Keyboard',
        'satuan': 'Pcs',
        'stock': 20,
        'harga': 150000
    },
    {
        'kode': 'A002',
        'jenis': 'Earpods',
        'satuan': 'Pcs',
        'stock': 15,
        'harga': 200000
    }
]

def read_stock():
    while True:
        print("===================== Daftar Stock Aksesoris =====================")
        print("[1] Menampilkan Seluruh Stock Aksesoris")
        print("[2] Menampilkan Stock Tertentu Aksesoris")
        print("[3] Kembali Ke Menu Utama")
        readStock = int(input('Pilih SUB MENU : '))

        if readStock == 1:
            print('================== Daftar Stock Gudang Aksesoris ==================\n')
            print('Kode\t| Jenis\t\t| Satuan\t| Stock\t\t| Harga')
            if len(listAksesoris) <= 0:
                print("Tidak Ada Data")
            else:
                for i in range(len(listAksesoris)):
                    print('{}\t| {}\t| {}\t\t| {}\t\t| {}'.format(listAksesoris[i]['kode'],listAksesoris[i]['jenis'],listAksesoris[i]['satuan'],listAksesoris[i]['stock'],listAksesoris[i]['harga']))
            continue

        elif readStock == 2:
            if len(listAksesoris) != 0:
                readKode = input('Masukkan Kode Aksesoris : ')
                for j, i in enumerate(listAksesoris):
                    if readKode == i['kode']:
                        print('================== Daftar Stock Gudang Aksesoris ==================\n')
                        print('Kode\t| Jenis\t\t| Satuan\t| Stock\t\t| Harga')
                        print('{}\t| {}\t| {}\t\t| {}\t\t| {}'.format(listAksesoris[j]['kode'],listAksesoris[j]['jenis'],listAksesoris[j]['satuan'],listAksesoris[j]['stock'],listAksesoris[j]['harga']))
                        read_stock()
                else:
                    print('Tidak Ada Stock Aksesoris')
                read_stock()

        elif readStock == 3:
            main_menu()

def create_stock():
    while True:
        print("==================== Menambah Stock Aksesoris ====================")
        print("[1] Menambah Stock Aksesoris")
        print("[2] Kembali Ke Menu Utama")
        createStock = int(input('Pilih SUB MENU : '))

        if createStock == 1:
            if len(listAksesoris) != 0:
                addKode = input('Masukkan Kode Aksesoris : ')
                for j, i in enumerate(listAksesoris):
                    if len(listAksesoris) != 0:
                        if addKode == i['kode']:
                            print('Aksesoris Sudah Ada')
                            create_stock()

                addJenis = input('Masukkan Jenis Aksesoris : ')
                addSatuan = input('Masukkan Satuan Aksesoris : ')
                addStock = int(input('Masukkan Stock Aksesoris : '))
                addHarga = int(input('Masukkan Harga Aksesoris : '))

                added = {
                    'kode' : '{}'.format(addKode),
                    'jenis' : '{}'.format(addJenis),
                    'satuan' : '{}'.format(addSatuan),
                    'stock' : '{}'.format(addStock),
                    'harga' : '{}'.format(addHarga),
                }
                print('Aksesoris yang ditambahkan : ', added)
                checkerCreate = input('\nApakah Data Akan Disimpan? (Y/N) : ').upper()
                if checkerCreate == 'Y':
                    listAksesoris.append(added)
                    print('\nAksesoris Berhasil Ditambahkan')
                elif checkerCreate == 'N':
                    print('\nAksesoris Tidak Ditambahkan')
                else:
                    break
            continue

        elif createStock == 2:
            main_menu()

def update_stock():
    while True:
        print("==================== Mengubah Stock Aksesoris ====================")
        print("[1] Mengubah Stock Aksesoris")
        print("[2] Kembali Ke Menu Utama")
        updateStock = int(input('Pilih SUB MENU : '))

        if updateStock == 1:
            if len(listAksesoris) != 0:
                updateKode = input('Masukkan Kode Aksesoris : ')
                for j, i in enumerate(listAksesoris):
                    if updateKode == i['kode']:
                        print('================== Daftar Stock Gudang Aksesoris ==================\n')
                        print('Kode\t| Jenis\t\t| Satuan\t| Stock\t\t| Harga')
                        print('{}\t| {}\t| {}\t\t| {}\t\t| {}'.format(listAksesoris[j]['kode'],listAksesoris[j]['jenis'],listAksesoris[j]['satuan'],listAksesoris[j]['stock'],listAksesoris[j]['harga']))
                        checkerUpdate = input('Apakah Ingin Mengubah Aksesoris Tersebut? (Y/N) : ').upper()
                        if checkerUpdate == 'Y':
                            colUpdate = input('Pilih Kolom yang Ingin Diubah : ')
                            if colUpdate == 'jenis':
                                newJenis = input('Masukkan Jenis Aksesoris Baru : ')
                                i['jenis'] = newJenis
                                print('Data Berhasil Diubah')
                                break
                            elif colUpdate == 'stock':
                                newStock = int(input('Masukkan Stock Aksesoris Baru : '))        
                                i['stock'] = newStock
                                print('Data Berhasil Diubah')
                                break
                            elif colUpdate == 'harga':
                                newHarga = int(input('Masukkan Harga Aksesoris Baru : '))                        
                                i['harga'] = newHarga
                                print('Data Berhasil Diubah')
                                break
                        elif checkerUpdate == 'N':
                            print('\nData Tidak Diubah')
                            break
                        else:
                            break           
                else:
                    print('Tidak Ada Stock Aksesoris')
                update_stock()

        elif updateStock == 2:
            main_menu()

def delete_stock():
    while True:
        print("==================== Menghapus Stock Aksesoris ====================")
        print("[1] Menghapus Stock Aksesoris")
        print("[2] Kembali Ke Menu Utama")
        deleteStock = int(input('Pilih SUB MENU : '))

        if deleteStock == 1:
            if len(listAksesoris) != 0:
                deleteKode = input('Masukkan Kode Aksesoris : ')
                for j, i in enumerate(listAksesoris):
                    if deleteKode == i['kode']:
                        print('================== Daftar Stock Gudang Aksesoris ==================\n')
                        print('Kode\t| Jenis\t\t| Satuan\t| Stock\t\t| Harga')
                        print('{}\t| {}\t| {}\t\t| {}\t\t| {}'.format(listAksesoris[j]['kode'],listAksesoris[j]['jenis'],listAksesoris[j]['satuan'],listAksesoris[j]['stock'],listAksesoris[j]['harga']))
                        checkerDelete = input('Apakah Yakin Ingin Menghapus Aksesoris Tersebut? (Y/N) : ').upper()
                        if checkerDelete == 'Y':
                            del listAksesoris[j]
                            print('\nData Berhasil Dihapus')
                            break
                        elif checkerDelete == 'N':
                            print('\nData Tidak Dihapus')
                            break
                        else:
                            break
                else:
                    print('Tidak Ada Stock Aksesoris')
                delete_stock()

        elif deleteStock == 2:
            main_menu()

def get_login():
    print('=' * 20)
    print('LOGIN STOCK GUDANG')
    username = input('USERNAME : ')
    password = input('PASSWORD : ')
 
    if username == 'admin' and password == 'adminpass':
        print('SUCCESS! \n')
        main_menu()
    else:
        print('UNSUCCESS! ')
        get_login()            

def main_menu():
    print("===================== Stock Gudang Aksesoris =====================")
    print("[1] Menampilkan Daftar Aksesoris")
    print("[2] Menambah Stock Aksesoris")
    print("[3] Mengubah Stock Aksesoris")
    print("[4] Menghapus Stock Aksesoris")
    print("[5] Exit")
    print("==================================================================")
    
    menu = int(input("PILIH MENU : "))

    if menu == 1:
        read_stock()
    elif menu == 2:
        create_stock()
    elif menu == 3:
        update_stock()
    elif menu == 4:
        delete_stock()
    elif menu == 5:
        print("TERIMA KASIH")
        exit()
    else:
        print("SALAH PILIH!")

if __name__ == "__main__":
    while(True):
        get_login()