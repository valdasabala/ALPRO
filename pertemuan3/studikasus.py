print("==== sistem cek belanja & status pembayaran ====")

nama_pembeli = input("Masukkan nama pembeli: ")
harga_barang = int(input("Harga satuan barang(Rp): "))
jumlah_barang = int(input("jumlah barang yang dibeli: "))
uang_dibayar = input("jumlah uang yang diberikan ke kasir: "))

total_harga = harga_barang * jumlah_barang
selisih = uang_bayar - total_harga


uang_cukup = harga_barang * jumlah_barang
uang_pas = uang_bayar - uang_cukup
uang_kurang = uang_cukup - uang_bayar

print("\n==== Ringkasan transaksi ====")
print("Nama Pelanggan:" + nama)
print("Harga Satuan Barang:Rp", harga_satuan)
total_harga = harga_satuan * jumlah_barang
print("Total Harga Barang:Rp", total_harga)

print("Uang yang dibayarkan:Rp", uang_bayar)
print("Selisih Uang:Rp", selisih)
print("Uang yang dibayarkan cukup:Rp", uang_pas)
print("Uang yang dibayarkan kurang:Rp", uang_kurang)    