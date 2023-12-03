import csv

def inventaris():
    try:
        with open('inventaris.csv', 'r',newline='')as file:
            baca = csv.DictReader(file)
            inventaris = {row['Nama Barang']: {'Jumlah' : int(row['Jumlah']), 'Deskripsi' : row['Deskripsi']} for row in baca}
    except FileNotFoundError:
        inventaris ={}
    return inventaris

def simpan_item(inventaris):
    with open('inventaris.csv', 'w', newline='')as file:
        data = ['Nama Barang','Jumlah','Deskripsi']
        tulis = csv.DictWriter(file, fieldnames=data)
        tulis.writeheader()
        for nama, a in inventaris.items():
            tulis.writerow(
                {'Nama Barang': nama, 'Jumlah': a['Jumlah'], 'Deskripsi': a['Deskripsi']}
            )

def tampilkan_barang(inventaris):
    for key in inventaris:
        jumlah = inventaris [key]['Jumlah']
        deskripsi = inventaris[key]['Deskripsi']
        print(f"Nama Barang\t\t: {key} \nJumlah\t\t\t: {jumlah}\nDeskripsi Barang\t: {deskripsi}\n\n")

def tambah_barang(inventaris):
    nama = input("Masukkan Nama Barang : ")
    jumlah = int(input("Masukkan Jumlah Barang : "))
    deskripsi = input("Masukkan Deskripsi Barang : ")

    if nama in inventaris :
        inventaris [nama]['Jumlah'] += jumlah
    else :
        inventaris [nama]={'Jumlah': jumlah, 'Deskripsi': deskripsi}
    print(f"{jumlah}, {nama}(s) berhasil ditambahkan !")

def cari_barang(inventaris):
    cari_nama = input("Mau cari barang apa?")
    if cari_nama in inventaris:
        print("\nNama Barang\t\t:", cari_nama)
        print("Jumlah\t\t\t:", inventaris[cari_nama]['Jumlah'])
        print("Deskripsi Barang\t:", inventaris[cari_nama]['Deskripsi'])

def hapus_item (inventaris):
    hapus_nama = input ("Masukkan nama barang yang ingin dihapus : ")
    if hapus_nama in inventaris :
        print ("Data berikut berhasil dihapus : ")
        print ("Nama Barang\t\t: ",hapus_nama)
        print("Jumlah\t\t\t:", inventaris[hapus_nama]['Jumlah'])
        print("Deskripsi Barang\t:", inventaris[hapus_nama]['Deskripsi'])
        del inventaris [hapus_nama]
        
    else : print("Barang tidak ditemukan\n")

# def statistik(inventaris):

inventaris = inventaris()

while True:
    print("\nManajemen Inventaris Barang:")
    print("1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Cari Barang")
    print("4. Hapus Barang")
    print("5. Statistik Inventaris")
    print("x. Exit")

    choice = input("Pilih Menu :")
    if choice == '1':
        print("\n\n===== Tambah Barang =====\n")
        tambah_barang(inventaris)
        simpan_item(inventaris)
    elif choice == '2':
        print("\n\n===== Tampilkan Barang =====\n")
        tampilkan_barang(inventaris)
    elif choice == '3':
        print("\n\n===== Cari Barang =====\n")
        cari_barang(inventaris)
    elif choice == '4':
        print("\n\n===== Hapus Barang =====\n")
        hapus_item(inventaris)
        simpan_item(inventaris)
    elif choice == '5':
        print("\n\n===== Statistik Inventaris =====\n")
    elif choice == 'x':
        break
