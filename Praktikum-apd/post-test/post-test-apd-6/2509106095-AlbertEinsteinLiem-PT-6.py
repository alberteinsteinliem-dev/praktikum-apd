import os

users = {
    "Albert Einstein Liem": {"password": "2509106095", "role": "admin"}
}

lomba = {
    1: {
        "nama": "Lomba Mobile Legends",
        "tanggal": "1 Januari 2025",
        "aturan": "Dilarang ngcheat",
        "hadiah": "Rp1.000.000"
    }
}


peserta = []

while True:
    os.system(("cls", "clear")[os.name != "nt"])
    print("=== DAFTAR LOMBA TAHUN BARU ===")
    print("=======================================")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("=======================================")
    menu = input("Pilih menu: ")

    if menu == "1":
        os.system(("cls", "clear")[os.name != "nt"])
        print("=== LOGIN ===")
        nama = input("Username: ")
        pw = input("Password: ")

        if nama in users and users[nama]["password"] == pw:
            role = users[nama]["role"]
            if role == "admin":
                while True:
                    os.system(("cls", "clear")[os.name != "nt"])
                    print("=== MENU ADMIN ===")
                    print("1. Lihat Semua Lomba")
                    print("2. Tambah Lomba")
                    print("3. Ubah Lomba")
                    print("4. Hapus Lomba")
                    print("5. Lihat Peserta")
                    print("6. Logout")
                    pilih = input("Pilih menu: ")

                    if pilih == "1":
                        os.system(("cls", "clear")[os.name != "nt"])
                        print("=== DAFTAR LOMBA ===")
                        if len(lomba) == 0:
                            print("Belum ada lomba terdaftar.")
                        else:
                            for i, data in lomba.items():
                                print(i, ".", data["nama"])
                                print(f"   Tanggal  : {data['tanggal']}")
                                print(f"   Peraturan: {data['aturan']}")
                                print(f"   Hadiah   : {data['hadiah']}")
                                print()
                        input("Pencet enter untuk lanjut")

                    elif pilih == "2":
                        os.system(("cls", "clear")[os.name != "nt"])
                        print("=== TAMBAH LOMBA BARU ===")
                        nama_lomba = input("Lomba: ")
                        hari = input("Hari lomba: ")
                        peraturan = input("Peraturan lomba: ")
                        hadiah = input("Hadiah lomba: ")
                        id_baru = len(lomba) + 1
                        data_lomba = {
                        "nama": nama_lomba,
                        "tanggal": hari,
                        "aturan": peraturan,
                        "hadiah": hadiah
                        }
                        lomba[id_baru] = data_lomba
                        print("Lomba berhasil ditambahkan!")
                        input("Pencet enter untuk lanjut")

                    elif pilih == "3":
                        os.system(("cls", "clear")[os.name != "nt"])
                        print("=== UBAH DATA LOMBA ===")
                        for i, data in lomba.items():
                           print(i, ".", data["nama"])
                        nomor = input("Nomor lomba yang mau diubah: ")
                        angka = True
                        for c in nomor:
                            angka = c in "0123456789"
                            if not angka:
                                angka = False
                        if angka and nomor != "":
                            nomor = int(nomor)
                            if nomor in lomba:
                                print("Masukkan data lomba baru:")
                                nama_baru = input("Nama : ")
                                tanggal_baru = input("Tanggal: ")
                                aturan_baru = input("Peraturan: ")
                                hadiah_baru = input("Hadiah: ")

                                if nama_baru: lomba[nomor]["nama"] = nama_baru
                                if tanggal_baru: lomba[nomor]["tanggal"] = tanggal_baru
                                if aturan_baru: lomba[nomor]["aturan"] = aturan_baru
                                if hadiah_baru: lomba[nomor]["hadiah"] = hadiah_baru
                                print("Data lomba berhasil diubah!")
                            else:
                                print("Nomor lomba tidak valid.")
                        else:
                            print("Input tidak valid.")
                        input("Pencet enter untuk lanjut")

                    elif pilih == "4":
                        os.system(("cls", "clear")[os.name != "nt"])
                        print("=== HAPUS LOMBA ===")
                        for i, data in lomba.items():
                           print(i, ".", data["nama"])
                        nomor = input("Nomor lomba yang ingin dihapus: ")
                        angka = True
                        for c in nomor:
                            angka = c in "0123456789"
                            if not angka:
                                angka = False
                        if angka and nomor != "":
                            nomor = int(nomor)
                            if nomor in lomba:
                                del lomba[nomor]
                                print("Lomba berhasil dihapus!")
                            else:
                                print("Nomor lomba tidak ditemukan.")
                        else:
                            print("Input tidak valid.")
                        input("Pencet enter untuk lanjut")

                    elif pilih == "5":
                        os.system(("cls", "clear")[os.name != "nt"])
                        print("=== DAFTAR PESERTA ===")
                        if len(peserta) == 0:
                            print("Belum ada peserta terdaftar.")
                        else:
                            for p in peserta:
                                print(f"{p['nama']} - {p['lomba']}")
                        input("Pencet enter untuk lanjut")

                    elif pilih == "6":
                        break

                    else:
                        print("Pilihan tidak valid!")
                        input("Pencet enter untuk lanjut")

            else:
                while True:
                    os.system(("cls", "clear")[os.name != "nt"])
                    print("=== MENU PENGGUNA ===")
                    print("1. Lihat Lomba")
                    print("2. Daftar Lomba")
                    print("3. Lihat Lomba yang Diikuti")
                    print("4. Logout")
                    pilih = input("Pilih menu: ")

                    if pilih == "1":
                        os.system(("cls", "clear")[os.name != "nt"])
                        print("=== DAFTAR LOMBA ===")
                        for i, data in lomba.items():
                            print(i, ".", data["nama"])
                            print(f"   Tanggal  : {data['tanggal']}")
                            print(f"   Peraturan: {data['aturan']}")
                            print(f"   Hadiah   : {data['hadiah']}")
                            print()
                        input("Pencet enter untuk lanjut")

                    elif pilih == "2":
                        os.system(("cls", "clear")[os.name != "nt"])
                        print("=== DAFTAR KE LOMBA ===")
                        for i, data in lomba.items():
                           print(i, ".", data["nama"])
                        nomor = input("Pilih nomor lomba yang kamu minati: ")
                        angka = True
                        for c in nomor:
                            angka = c in "0123456789"
                            if not angka:
                                angka = False
                        if angka and nomor != "":
                            nomor = int(nomor)
                            if nomor in lomba:
                                peserta.append({"nama": nama, "lomba": lomba[nomor]["nama"]})
                                print(f"Berhasil mendaftar ke {lomba[nomor]['nama']}!")
                            else:
                                print("Nomor lomba tidak valid.")
                        else:
                            print("Input tidak valid.")
                        input("Pencet enter untuk lanjut")

                    elif pilih == "3":
                        os.system(("cls", "clear")[os.name != "nt"])
                        print("=== LOMBA YANG DIIKUTI ===")
                        ada = False
                        for p in peserta:
                            if p["nama"] == nama:
                                print("-", p["lomba"])
                                ada = True
                        if not ada:
                            print("Belum daftar lomba apapun.")
                        input("Pencet enter untuk lanjut")

                    elif pilih == "4":
                        break

                    else:
                        print("Pilihan tidak valid!")
                        input("Pencet enter untuk lanjut")

        else:
            print("Login gagal! Username atau password salah.")
            input("Pencet enter untuk lanjut")

    elif menu == "2":
        os.system(("cls", "clear")[os.name != "nt"])
        print("=== REGISTER AKUN BARU ===")
        nama = input("Masukkan username baru: ")
        pw = input("Masukkan password baru: ")
        if nama not in users:
            users[nama] = {"password": pw, "role": "user"}
            print("Akun sudah dibuat")
        else:
            print("Username sudah digunakan.")
        input("Pencet enter untuk lanjut")

    elif menu == "3":
        os.system(("cls", "clear")[os.name != "nt"])
        print("Terimakasih! Semoga beruntung!!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Pencet enter untuk lanjut")
