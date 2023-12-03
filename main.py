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

def tambah_item(inventaris):
    nama = input("Masukkan Nama Barang : ")
    jumlah = int(input("Masukkan Jumlah Barang : "))
    deskripsi = input("Masukkan Deskripsi Barang : ")

    if nama in inventaris :
        inventaris [nama]['Jumlah'] += jumlah
    else :
        inventaris [nama]={'Jumlah': jumlah, 'Deskripsi': deskripsi}
    print(f"{jumlah}, {nama}(s) berhasil ditambahkan !")


inventaris = inventaris()

while True:
    print("\nManajemen Inventaris Barang:")
    print("1. Tambah Barang")
    print("x. Exit")

    choice = input("Pilih Menu :")
    if choice == '1':
        tambah_item(inventaris)
        simpan_item(inventaris)
    elif choice == 'x':
        break