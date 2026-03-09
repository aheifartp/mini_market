from services import db
from services import libs

def add():
    kode_barang = input('kode barang: ')
    nama_barang = input('nama barang: ')
    harga_barang = int(input('harga barang: '))
    stok_barang = int(input('stok barang: '))
    
    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)

def check():
    items = db.fetch_item()
    for item in items:
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        print(f'''
kode {kode_barang}
{nama_barang} | Rp {harga_barang}
stok: {stok_barang}           
''')
    
def start():
    while True:
        menu = int(input('menu:\n\n1. Tambah Barang\n2. Check Barang\n3. Kembali\n4. Hapus Barang\n\nsilahkan pilih:'))
        
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            libs.exit_program()
        elif menu == 4:
            delete()
        else:
            break    
        
def delete():
    kode_barang = input('kode barang yang ingin dihapus: ')
    db.delete_item(kode_barang) 
    
if __name__ == '__main__':
    libs.welcome_message()
    start()