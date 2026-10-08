print("==== kalkulator patungan makan ====")


nama = input("Masukkan nama Anda: ")
tagihan = int(input("Masukkan tagihan: "))
persen = int(input("Masukkan persen: "))
jumlah_orang = int(input("Masukkan jumlah orang: "))

nominal_tip = tagihan * persen / 100
total_tagihan = tagihan + nominal_tip
bayar_per_orang = total_tagihan / jumlah_orang
print("\n==== Rincian Tagihan ====")
print("Nama Pembeli:" + nama)
print("Total Tagihan Beserta Tip:Rp", total_tagihan)
print("Setiap orang harus membayar:Rp", bayar_per_orang)
