def tampilkan_data():
    # Data diri
    data_diri = {
        1: "Nama: Putra Ramadhan",
        2: "Umur: 19",
        3: "Program Studi: PTI 2 C"
    }

    # Tampilkan opsi yang tersedia
    print("Pilih angka untuk menampilkan data:")
    print("1 - Nama")
    print("2 - Umur")
    print("3 - Program Studi")

    # Ambil input dari pengguna
    pilihan = int(input("Masukkan pilihan (1/2/3): "))

    # Tampilkan data sesuai pilihan pengguna
    if pilihan in data_diri:
        print(data_diri[pilihan])
    else:
        print("Pilihan tidak valid.")

# Panggil fungsi untuk menjalankan program
tampilkan_data()