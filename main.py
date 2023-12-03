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
    if len(inventaris) != 0:
        for key in inventaris:
            jumlah = inventaris [key]['Jumlah']
            deskripsi = inventaris[key]['Deskripsi']
            print(f"Nama Barang\t\t: {key} \nJumlah\t\t\t: {jumlah}\nDeskripsi Barang\t: {deskripsi}\n\n")
    else:
        print("Tidak ada barang dalam inventaris")
        
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
    cari_nama = input("Mau cari barang apa? ")
    if cari_nama in inventaris:
        print("\nNama Barang\t\t:", cari_nama)
        print("Jumlah\t\t\t:", inventaris[cari_nama]['Jumlah'])
        print("Deskripsi Barang\t:", inventaris[cari_nama]['Deskripsi'])
    else: 
        print("Barang tidak ditemukan\n")

def hapus_barang (inventaris):
    hapus_nama = input ("Masukkan nama barang yang ingin dihapus : ")
    if hapus_nama in inventaris :
        print ("Data berikut berhasil dihapus : ")
        print ("Nama Barang\t\t:",hapus_nama)
        print("Jumlah\t\t\t:", inventaris[hapus_nama]['Jumlah'])
        print("Deskripsi Barang\t:", inventaris[hapus_nama]['Deskripsi'])
        del inventaris [hapus_nama]
    else:
        print("Barang tidak ditemukan\n")

def statistik(inventaris):
    jumlah_jenis_barang = len(inventaris)
    if jumlah_jenis_barang != 0:
        list_jumlah_barang = []
        for key in inventaris:
            list_jumlah_barang.append(inventaris[key]['Jumlah'])
        jumlah_barang = sum(list_jumlah_barang)
        rata_rata = jumlah_barang / jumlah_jenis_barang
        jumlah_min = min(list_jumlah_barang)
        jumlah_max = max(list_jumlah_barang)
        for key in inventaris:
            if inventaris[key]['Jumlah'] == jumlah_min:
                nama_barang_min = key
            if inventaris[key]['Jumlah'] == jumlah_max:
                nama_barang_max = key
        print("Jumlah Jenis Barang\t\t:", jumlah_jenis_barang)
        print("Jumlah Total Barang\t\t:", jumlah_barang)
        print("Rata-rata Setiap Barang\t\t:", rata_rata)
        print(f"Barang dengan jumlah terbesar\t: {nama_barang_max} ({jumlah_max})")
        print(f"Barang dengan jumlah terkecil\t: {nama_barang_min} ({jumlah_min})")
    else:
        print("Tidak ada barang dalam inventaris")

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
        hapus_barang(inventaris)
        simpan_item(inventaris)
    elif choice == '5':
        print("\n\n===== Statistik Inventaris =====\n")
        statistik(inventaris)
    elif choice == 'x':
        break