nama_restoran = "Restoran suka-suka"
jenis_makanan = "Makanan berat"
restoran_buka = True
rating_restoran = 4.5


print("---FORM PEMESANAN RESTORAN---")
nama_pelanggan = input("Masukkan nama pelanggan: ")
nomor_meja = input("Masukkan nomor meja: ")
nama_makanan = input("Masukkan nama makanan: ")
jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
harga_makanan = 25000


print("\n---INFORMASI RESTORAN---")
print("Nama Restoran:", nama_restoran)
print("Jenis Makanan:", jenis_makanan)
print("Restoran sedang buka")
print("Rating Restoran:", rating_restoran)

print("\n---DETAIL PEMESANAN---")
print("Nama Pelanggan:", nama_pelanggan)
print("Nomor Meja:", nomor_meja)
print("Nama Makanan:", nama_makanan)
print("Jumlah Pesanan:", jumlah_pesanan)
print("Harga Makanan: Rp", harga_makanan)
print("Total Harga: Rp", jumlah_pesanan * harga_makanan) 
print("Terima kasih telah memesan di", nama_restoran, "!") 

print("\n---TIPE DATA---")
print("Tipe data nama_restoran:", type(nama_restoran))
print("Tipe data jenis_makanan:", type(jenis_makanan))
print("Tipe data restoran_buka:", type(restoran_buka))
print("Tipe data rating_restoran:", type(rating_restoran))
print("Tipe data nama_pelanggan:", type(nama_pelanggan))
print("Tipe data nomor_meja:", type(nomor_meja))
print("Tipe data nama_makanan:", type(nama_makanan))
print("Tipe data jumlah_pesanan:", type(jumlah_pesanan))
print("Tipe data harga_makanan:", type(harga_makanan))
print("Tipe data total_harga:", type(jumlah_pesanan * harga_makanan))