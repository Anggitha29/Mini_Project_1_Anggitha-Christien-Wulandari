data_pengunjung = []

while True:
    print("SISTEM PENDATAAN PENGUNJUNG PERPUSTAKAAN")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("Tambah Data")
        nama = input("Nama: ")
        nim = input("NIM: ")
        prodi = input("Prodi: ")
        keperluan = input("Keperluan: ")

        data = (nama, nim, prodi, keperluan)
        data_pengunjung.append(data)

        print("Data berhasil ditambahkan.")

    elif pilihan == "2":
        print("Data Pengunjung")

        if data_pengunjung == []:
            print("Belum ada data.")
        else:
            for data in data_pengunjung:
                print(data)

    elif pilihan == "3":
        print("Ubah Data")

        if data_pengunjung == []:
            print("Belum ada data.")
        else:
            while True:
                nim = input("Masukkan NIM yang ingin diubah: ")
                ditemukan = False
                posisi = 0

                for data in data_pengunjung:
                    if data[1] == nim:
                        ditemukan = True
                        break
                    posisi = posisi + 1

                if ditemukan == True:
                    break
                else:
                    print("NIM tidak ditemukan. Silakan coba lagi.")

            nama = input("Nama baru: ")
            nim_baru = input("NIM baru: ")
            prodi = input("Prodi baru: ")
            keperluan = input("Keperluan baru: ")

            data_pengunjung[posisi] = (nama, nim_baru, prodi, keperluan)

            print("Data berhasil diubah.")

    elif pilihan == "4":
        print("Hapus Data")

        if data_pengunjung == []:
            print("Belum ada data.")
        else:
            while True:
                nim = input("Masukkan NIM yang ingin dihapus: ")
                ditemukan = False

                for data in data_pengunjung:
                    if data[1] == nim:
                        ditemukan = True
                        break

                if ditemukan == True:
                    break
                else:
                    print("NIM tidak ditemukan. Silakan coba lagi.")

            data_pengunjung.remove(data)

            print("Data berhasil dihapus.")

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")