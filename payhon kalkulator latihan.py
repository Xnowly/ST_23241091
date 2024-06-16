print("Kalkulator Penjumlahan dan Pengurangan")
print("1. Penjumlahan")
print("2. Pengurangan")
# Memilih operasi
operasi = int(input("Pilih operasi: ")) 
# Memasukkan angka
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
# Melakukan operasi
if operasi == 1:
    hasil = angka1 + angka2
    operasi_kalkulator= "penjumlahan"
elif operasi == 2:
    hasil = angka1 - angka2
    operasi_kalkulator = "pengurangan"
    
print(f"Hasil dari {operasi_kalkulator} antara {angka1} dan {angka2} adalah: {hasil}")