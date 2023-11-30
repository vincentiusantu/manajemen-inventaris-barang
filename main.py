import csv

def inventaris():
    try:
        with open('inventaris.csv', 'r',newline=' ')as file:
            baca = csv.DictReader(file)
            inventaris = {row['Nama Barang']: {'Jumlah' : int(row['Jumlah']), 'Deskripsi' : row['Deskripsi']} for row in baca}
    except FileNotFoundError:
        inventaris ={}
    return inventaris

def simpan_item(inventaris):
    with open('inventaris.csv', 'w', newline=' ')as file:
        data = ['Nama','Jumlah','Deskripsi']
        tulis = csv.DictWriter(file, data=data)
        tulis.writeheader()
        for nama, a in inventaris.item():
            tulis.writerow(
                {'Nama Barang': nama, 'Jumlah': a['Jumlah'], 'Deskripsi': a['Deskripsi']}
            )

def tambah_item(inventaris):
