#soal 1: string cleaning, type casting & formatting
#diberikan input string mentah dari user yang mengandung spasi tidak teratur: raw _price ="  4500  "
#intruksi
#1. bersihkan spasi di awal dan akhir string menggunakan method .strip()
raw_price = "  4500  "
clean_price = raw_price.strip()
print(f"Hasil strip: '{clean_price}'")
#2.konversikan string tersebut menjadi tipe integer
raw_price = "  45000 "
clean_price = raw_price.strip()
price = int(clean_price)
print(f"Hasil strip: '{clean_price}'")
print(f"Tipe: {type(price).__name__}, nilai: {price}")
#3. buat variable jumlah = 3 dan hitung total_harga = harga * jumlah
jumlah = 3
total_harga = price * jumlah
print(f"Total harga: {total_harga}")
#4. tampilkan kalimat berikut menggunakan f-string: harga satuan: Rp45000, jumlah: 3, total harga: Rp135000 (petunjuk: gunakan format ribuan :, jika memungkinkan)
print(f"harga satuan: Rp{price:,}, jumlah: {jumlah}, total harga: Rp{total_harga:,}")

print()

#soal 2: mutability test (tuple vs list)
#diberikan dua variable berikut: titik_koordinat = (10,20) daftar_skor = [80,90,85]
#intruksi
#1. coba ubah elemen pertama dari titik_koordinat menjadi 1 menggunakan mekanisme try-except untuk menangkap error yang type error, lalu cetak pesan penjelasanya
titik_koordinat = (10, 20)
try:
    titik_koordinat[0] = 1
except TypeError as e:
    print(f"Error: {e}. Tidak dapat mengubah elemen pada tuple.")
#2. ubah elemen pertama dari daftar_skor menjadi 88.
daftar_skor = [80, 90, 85]
daftar_skor[0] = 88
print(f"Daftar skor setelah diubah: {daftar_skor}")
#3. tuliskan kode untuk mengubah titik_koordinat menjadi list, ubah nilai pertamanya menjadi 15, lalu kembalikan lagi menjadi tuple.
titik_koordinat_list = list(titik_koordinat)
titik_koordinat_list[0] = 15
titik_koordinat = tuple(titik_koordinat_list)

print()

#soal 3: advance slicing & negative indexing
#diberikan string variabel berikut: teks = "PemrogramanPython2026"
#intruksi
#1. ambil kata "Python" menggunakan slicing positif.
teks = "PemrogramanPython2026"
kata_python = teks[13:19]
print(f"Kata yang diambil (positif): {kata_python}")
#2. ambil karakter "2026" menggunakan negative indexing/slicing.
karakter_2026 = teks[-4:]
print(f"Karakter yang diambil (negatif): {karakter_2026}")
#3. balikan seluruh karakter pada variable teks sehingga menjadi "6202nohtyPnamargormeP" ,menggunakan teknik slicing.
teks_terbalik = teks[::-1]
print(f"Teks yang dibalik: {teks_terbalik}")

print()

#soal 4: list manipulation & method comparasion
#diberikan daftar angka acak: nilai = [45,90,75,90,60,85]
#intruksi
#1. cetak nilai tertinggi (max()) dan berapa kali nilai 90 muncul (count()).
nilai = [45, 90, 75, 90, 60, 85]
print(f"Nilai tertinggi: {max(nilai)}")
print(f"Jumlah kemunculan 90: {nilai.count(90)}")
#2. gunakan fungsi sorted(nilai) dan simpan di variable nilai_baru. cetak variabel nilai asli dan nilai_baru untuk melihat perbedaanya.
nilai_baru = sorted(nilai)
print(f"Nilai asli: {nilai}")
print(f"Nilai baru: {nilai_baru}")
#3. gunakan method nilai.sort(reverse=True) pada list asli, lalu cetak variable nilai untuk membuktikan bahwa .sort() mengubah data secara in-place.
nilai.sort(reverse=True)
print(f"Nilai setelah sort in-place: {nilai}")

print()

#soal 5: string inspection & tuple unpacking
#diberikan tuple data penggunaan: user_info = ("Budi Santoso", "budi@email.com", "Surabaya")
#intruksi
#1. lakukan tuple unpacking untuk memasukan nilai di atas ke dalam variable nama, email, dan kota.
user_info = ("Budi Santoso", "budi@email.com", "Surabaya")
nama, email, kota = user_info
print("Nama:", nama)
print("Email:", email)
print("Kota:", kota)
#2. periksa apakah kata "surabaya" (huruf kecil semua) ada di dalam variabel kota menggunakan operator in. (petunjuk: Gunakan  .lower() agar pencarian bersifat case-insentive/tidak sensitif huruf besar-kecil)
print("surabaya" in kota.lower())
#3. cetak kalimat: "User Budi Santoso berasal dari SURABAYA" (kota diubah ke huruf kapital dengan .upper())
print(f"User {nama} berasal dari {kota.upper()}")   

print()

#soal 6: collection mastery (dictionary & set) 
#diberikan data pendaftaran seminar dalam bentuk list yang mengandung duplikat: peserta_raw = ["Budi", "Siti", "Andi', "Budi", "Siti", "Dewi"]
#intruksi
#1. hilangkan nama duplikat dari peserta_raw dengan mengonversinya ke bentuk Set, lalu konversi kembali menjadi List bernama peserta_unik.
peserta_raw = ["Budi", "Siti", "Andi", "Budi", "Siti", "Dewi"]
peserta_unik = list(set(peserta_raw))
print("Peserta unik:", peserta_unik)
#2. buat sebuah dictionary untuk menyimpan detail acara: acara = { "judul": "Workshop Python", "Kuota": 10, "peserta_unik": peserta_unik }
acara = {
    "judul": "Workshop Python",
    "Kuota": 10,
    "peserta_unik": peserta_unik
}

print("Detail acara:", acara)
#3. tambahkan key baru "status" dengan nilai "Tersedia" ke dalam dictionary acara.
acara["status"] = "Tersedia"
print("Detail acara setelah ditambahkan status:", acara)
#4. hitung sisa kuota (kuota - jumlah peserta unik) dan tampilkan informasi menggunakan f-string dan escape character \n: === DETAIL ACARA === JUDUL: Workshop Python Sisa Kuota: 6
sisa_kuota = acara["Kuota"] - len(acara["peserta_unik"])
print(f"=== DETAIL ACARA ===\nJUDUL: {acara['judul']}\nSisa Kuota: {sisa_kuota}")
