# 1. Kamu sedang marathon TV series di netflix
#    1 episode berdurasi 35 min dengan total 10 episode
#    berapa jam kamu menonton TV series tersebut?

total_menit = 35 * 10
jam = total_menit / 60
print("Total jam menonton:", jam, "jam")

# 2. Kamu ingin membeli cupang dg harga 10rb dan koi dg harga 20rb
# uang yg kamu bawa sebesar Rp.XXX000 (ganti XXX dg 3 angka terakhir NIM + 100)
# kamu hanya beli 5 cupang dan 2 koi
# berapa sisa uang kamu?

# NIM = 119 -> XXX = 119 + 100 = 219
uang = 219000
harga_cupang = 10000
harga_koi = 20000

beli_cupang = 5 * harga_cupang
beli_koi = 2 * harga_koi
total_belanja = beli_cupang + beli_koi
sisa_uang = uang - total_belanja 
print("Sisa uang:", sisa_uang)

# 3. Kamu ingin pergi liburan dg sepeda motor
# total jarak perjalanan XXX KM (ganti XXX dg 3 angka terakhir NIM)
# konsumsi BBM sepeda motor 2.7 KM per Liter
# kapasitas tangki sepeda motor X Liter (ganti X dg 1 angka terakhir NIM)
# harga bensin per liter Rp.1XXX0 (ganti XXX dg 3 angka terakhir NIM)
# jika total bensin yg dibutuhkan > 3 liter, maka dapat diskon Rp.500 per liter
# berapa total bensin yg dibutuhkan, harga bensin per liter setelah diskon (jika ada)-
# total biaya bensin, dan prakiraan berapa kali kamu harus mengisi bensin (dengan asumsi tangki penuh setiap kali isi)?
# NB: HARUS PAKAI INPUT !!!!!


# NIM = 119
# Jarak = 119 KM
# Kapasitas tangki = 9 Liter
# Harga bensin = Rp.11190

jarak = int(input("Masukkan total jarak perjalanan (KM): "))
konsumsi = 2.7 # KM per liter
tangki = int(input("Masukkan kapasitas tangki (liter): "))
harga_bensin = int(input("Masukkan harga bensin per liter: "))

# Hitung kebutuhan bensin
bensin_dibutuhkan = jarak / konsumsi

# cek diskon
if bensin_dibutuhkan > 3:
    harga_per_liter = harga_bensin - 500
else:
    harga_per_liter = harga_bensin

# Hitung biaya total
biaya_total = bensin_dibutuhkan * harga_per_liter

# Hitung berapa kali isi bensin
import math 
isi_ulang = math.ceil(bensin_dibutuhkan / tangki)

print("Total bensin yang dibutuhkan:", round(bensin_dibutuhkan, 2), "liter")
print("Harga bensin per liter setelah diskon:", harga_per_liter)
print("Total biaya bensin:", round(biaya_total, 2))
print("Perkiraan isi ulang bensin:", isi_ulang, "kali")