import os

user = [["Albert Einstein Liem", "2509106095", "Albert Einstein Liem"]]
peserta = []
lomba = [["Turnament Mobile Legend", "1 Januari 2025", "Tidak boleh cheat", "Hadiah uang Rp1.000.000"]]

while True:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("=== DAFTAR LOMBA TAHUN BARU ===")
    print("=======================================")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("=======================================")
    menu = input("pilih menu : ")

    if menu == "1":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print()
        print("=== LOGIN AKUN ===")
        print()
        nama = input("Username: ")
        pw = input("Password: ")

        akun = None
        i = 0
        while i < len(user):
            if nama == user[i][0] and pw == user[i][1]:
                akun = user[i]
                break
            i += 1

        if akun is None:
            print("Login gagal! Username atau password salah.")
            input("Pencet enter untuk lanjut")
        else:
            if akun[2] == "Albert Einstein Liem":
                while True:
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")

                    print()
                    print("=== MENU ADMIN ===")
                    print()
                    print("1. Lihat Semua Lomba")
                    print("2. Tambah Lomba")
                    print("3. Ubah Lomba")
                    print("4. Hapus Lomba")
                    print("5. Lihat Peserta")
                    print("6. Logout")
                    print()
                    pilih = input("Pilih menu: ")

                    if pilih == "1":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("=== DAFTAR LOMBA ===")
                        i = 0
                        while i < len(lomba):
                            print(i + 1, ".", lomba[i][0])
                            print("Tanggal Mulai :", lomba[i][1])
                            print("   Peraturan  :", lomba[i][2])
                            print("   Hadiah     :", lomba[i][3])
                            print()
                            i += 1
                        input("Pencet enter untuk lanjut")

                    elif pilih == "2":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("=== TAMBAH LOMBA BARU ===")
                        nama_lomba = input(" Lomba: ")
                        tanggal = input("Hari lomba: ")
                        aturan = input("Peraturan lomba: ")
                        hadiah = input("Hadiah lomba: ")
                        lomba.append([nama_lomba, tanggal, aturan, hadiah])
                        print("Lomba berhasil ditambahkan!")
                        input("Pencet enter untuk lanjut")

                    elif pilih == "3":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("=== UBAH DATA LOMBA ===")
                        i = 0
                        while i < len(lomba):
                            print(i + 1, ".", lomba[i][0])
                            i += 1
                        ganti = input("Pilih no lomba yang ingin di ubah: ")
                        digits = ''
                        for c in ganti:
                            if c.isdigit():
                                digits += c
                        angka = int(digits) - 1

                        if angka >= 0 and angka < len(lomba):
                            print("Data sebelumnya:")
                            print(f"Nama     : {lomba[angka][0]}")
                            print(f"Tanggal  : {lomba[angka][1]}")
                            print(f"Peraturan: {lomba[angka][2]}")
                            print(f"Hadiah   : {lomba[angka][3]}")
                            print("Masukkan data baru ")
                            nama_lomba = input("Lomba baru: ")
                            tanggal = input("Tanggal mulai lomba baru: ")
                            aturan = input("Peraturan baru: ")
                            hadiah = input("Hadiah baru: ")
                            if nama_lomba != "": lomba[angka][0] = nama_lomba
                            if tanggal != "": lomba[angka][1] = tanggal
                            if aturan != "": lomba[angka][2] = aturan
                            if hadiah != "": lomba[angka][3] = hadiah
                            print("Data lomba berhasil diubah!")
                        else:
                            print("Nomor lomba tidak valid.")
                        input("Pencet enter untuk lanjut")

                    elif pilih == "4":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("=== HAPUS LOMBA ===")
                        i = 0
                        while i < len(lomba):
                            print("{}. {}".format(i + 1, lomba[i][0]))
                            i += 1
                        hapus = input("Nomor lomba yang mau dihapus: ")
                        angka = int(''.join([c for c in hapus if c.isdigit()])) - 1
                        if angka >= 0 and angka < len(lomba):
                            del lomba[angka]
                            print("Lomba berhasil dihapus!")
                        else:
                            print("Nomor lomba tidak valid.")
                        input("Pencet enter untuk lanjut")

                    elif pilih == "5":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("=== DAFTAR PESERTA ===")
                        if peserta == []:
                            print("Belum ada peserta yang mendaftar.")
                        else:
                            for p in peserta:
                                print(p[0], "-", p[1])
                        input("Pencet enter untuk lanjut")

                    elif pilih == "6":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("Pencet enter untuk lanjut")

            else:
                while True:
                    if os.name == "nt":
                        os.system("cls")
                    else:
                        os.system("clear")

                    print()
                    print("=== MENU PENGGUNA ===")
                    print()
                    print("1. Lihat Lomba")
                    print("2. Daftar Lomba")
                    print("3. Lihat Lomba yang Diikuti")
                    print("4. Logout")
                    print()
                    pilih = input("Pilih menu: ")

                    if pilih == "1":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("=== DAFTAR LOMBA ===")
                        for i, l in enumerate(lomba):
                            print(f"{i+1}. {l[0]}")
                            print(f"   Tanggal Mulai : {l[1]}")
                            print(f"   Peraturan     : {l[2]}")
                            print(f"   Hadiah        : {l[3]}")
                            print()
                        input("Pencet enter untuk lanjut")

                    elif pilih == "2":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("=== DAFTAR KE LOMBA ===")
                        for i, l in enumerate(lomba):
                            print("Nomor", i+1, ":", l[0])
                        pilihan_lomba = input("Pilih nomor lomba yang kamu minati: ")
                        nomor = int(pilihan_lomba) - 1
                        if nomor >= 0 and nomor < len(lomba):
                            peserta.append([akun[0], lomba[nomor][0]])
                            print(f"Berhasil mendaftar ke {lomba[nomor][0]}!")
                        else:
                            print("Nomor lomba tidak valid.")
                        input("Pencet enter untuk lanjut")

                    elif pilih == "3":
                        if os.name == "nt":
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("=== LOMBA YANG DIIKUTI ===")
                        ada = False
                        for p in peserta:
                            if p[0] == akun[0]:
                                print(f"- {p[1]}")
                                ada = True
                        if not ada:
                            print("Belum daftar lomba apapun.")
                        input("Pencet enter untuk lanjut")

                    elif pilih == "4":
                        break
                    else:
                        print("Pilihan tidak valid!")
                        input("Pencet enter untuk lanjut")

    elif menu == "2":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print()
        print("=== REGISTER AKUN BARU ===")
        print()
        nama = input("Masukkan username baru: ")
        pw = input("Masukkan password baru: ")
        role = "user"
        user.append([nama, pw, role])
        print("Akun sudah di buat")
        input("Pencet enter untuk lanjut")

    elif menu == "3":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("Terimakasih! Semoga beruntung!!")
        break

    else:
        print("Pilihan tidak valid")
        input()