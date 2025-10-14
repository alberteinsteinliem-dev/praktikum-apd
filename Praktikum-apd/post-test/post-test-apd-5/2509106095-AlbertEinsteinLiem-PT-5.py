import os

user = [["Albert Einstein Liem", "2509106095", "Albert Einstein Liem"]]
peserta = []
lomba = [["Turnament Mobile Legend", "1 Januari 2025", "Tidak boleh cheat", "Hadiah uang Rp1.000.000"]]

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
     os.system("clear")

def garis():
    print("")

def pause():
    input("Tekan Enter untuk melanjutkan...")

def ubah_jadi_angka(teks):
    angka = 0
    for t in teks:
        if t >= "0" and t <= "9":
            angka = angka * 10 + int(t)
    return angka

def register():
    clear()
    garis()
    print("=== REGISTER AKUN BARU ===")
    garis()
    nama = input("Masukkan username baru: ")
    pw = input("Masukkan password baru: ")
    role = "user"
    user.append([nama, pw, role])
    print("Akun lomba anda sudah dibuat")
    pause()

def login():
    clear()
    garis()
    print("=== LOGIN AKUN ===")
    garis()
    nama = input("Username: ")
    pw = input("Password: ")
    i = 0
    while i < len(user):
        if nama == user[i][0] and pw == user[i][1]:
            return user[i]
        i += 1
    print("Login gagal! Username atau password salah.")
    pause()
    return None

def menu_admin():
    while True:
        clear()
        garis()
        print("=== MENU ADMIN ===")
        garis()
        print("1. Lihat Semua Lomba")
        print("2. Tambah Lomba")
        print("3. Ubah Lomba")
        print("4. Hapus Lomba")
        print("5. Lihat Peserta")
        print("6. Logout")
        garis()
        pilih = input("Pilih menu: ")

        if pilih == "1":
            clear()
            print("=== DAFTAR LOMBA ===")
            i = 0
            while i < len(lomba):
                print(i + 1, ".", lomba[i][0])
                print("Tanggal Mulai :", lomba[i][1])
                print("   Peraturan  :", lomba[i][2])
                print("   Hadiah     :", lomba[i][3])
                print()
                i += 1
            pause()

        elif pilih == "2":
            clear()
            print("=== TAMBAH LOMBA BARU ===")
            nama = input(" Lomba: ")
            tanggal = input("Hari lomba: ")
            aturan = input("Peraturan lomba: ")
            hadiah = input("Hadiah lomba: ")
            lomba.append([nama, tanggal, aturan, hadiah])
            print("Lomba berhasil ditambahkan!")
            pause()

        elif pilih == "3":
            clear()
            print("=== UBAH DATA LOMBA ===")
            i = 0
            while i < len(lomba):
                print(i + 1, ".", lomba[i][0])
                i += 1

            ganti = input("Pilih no lomba yang ingin di ubah: ")
            angka = ubah_jadi_angka(ganti) - 1

            if angka >= 0 and angka < len(lomba):
                print("Data sebelumnya:")
                print(f"Nama     : {lomba[angka][0]}")
                print(f"Tanggal  : {lomba[angka][1]}")
                print(f"Peraturan: {lomba[angka][2]}")
                print(f"Hadiah   : {lomba[angka][3]}")
                print("Masukkan data baru ")
                nama = input("Lomba baru: ")
                tanggal = input("Tanggal mulai lomba baru: ")
                aturan = input("Peraturan baru: ")
                hadiah = input("Hadiah baru: ")

                if nama != "": lomba[angka][0] = nama
                if tanggal != "": lomba[angka][1] = tanggal
                if aturan != "": lomba[angka][2] = aturan
                if hadiah != "": lomba[angka][3] = hadiah
                print("Data lomba berhasil diubah!")
            else:
                print("Nomor lomba tidak valid.")
            pause()

        elif pilih == "4":
            clear()
            print("=== HAPUS LOMBA ===")
            i = 0
            while i < len(lomba):
                print("{}. {}".format(i + 1, lomba[i][0]))
                i += 1

            hapus = input("Nomor lomba yang mau dihapus: ")
            angka = ubah_jadi_angka(hapus) - 1

            if angka >= 0 and angka < len(lomba):
                del lomba[angka]
                print("Lomba berhasil dihapus!")
            else:
                print("Nomor lomba tidak valid.")
            pause()

        elif pilih == "5":
            clear()
            print("=== DAFTAR PESERTA ===")
            if peserta == []:
                print("Belum ada peserta yang mendaftar.")
            else:
                i = 0
                while i < len(peserta):
                    print(peserta[i][0], "-", peserta[i][1])
                    i += 1
            pause()

        elif pilih == "6":
            break
        else:
            print("Pilihan tidak valid!")
            pause()

def menu_user(nama_user):
    while True:
        clear()
        garis()
        print("=== MENU PENGGUNA ===")
        garis()
        print("1. Lihat Lomba")
        print("2. Daftar Lomba")
        print("3. Lihat Lomba yang Diikuti")
        print("4. Logout")
        garis()
        pilih = input("Pilih menu: ")

        if pilih == "1":
            clear()
            print("=== DAFTAR LOMBA ===")
            i = 0
            while i < len(lomba):
                print("{}. {}".format(i + 1, lomba[i][0]))
                print(f"   Tanggal Mulai : {lomba[i][1]}")
                print(f"   Peraturan     : {lomba[i][2]}")
                print(f"   Hadiah        : {lomba[i][3]}")
                print()
                i += 1
            pause()

        elif pilih == "2":
            clear()
            print("=== DAFTAR KE LOMBA ===")
            i = 0
            while i < len(lomba):
                print("{}. {}".format(i + 1, lomba[i][0]))
                i += 1

            pilihan_lomba = input("Pilih nomor lomba yang kamu minati: ")
            nomor = int(pilihan_lomba) - 1

            if nomor >= 0 and nomor < len(lomba):
                peserta.append([nama_user, lomba[nomor][0]])
                print(f"Berhasil mendaftar ke {lomba[nomor][0]}!")
            else:
                print("Nomor lomba tidak valid.")
            pause()

        elif pilih == "3":
            clear()
            print("=== LOMBA YANG DIIKUTI ===")
            ada = False
            i = 0
            while i < len(peserta):
                if peserta[i][0] == nama_user:
                    print(f"- {peserta[i][1]}")
                    ada = True
                i += 1
            if not ada:
                print("Anda belum mendaftar lomba apa pun.")
            pause()

        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid!")
            pause()

while True:
    clear()
    print("=== PENDAFTARAN LOMBA TAHUN BARU ===")
    print("=======================================")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    print("=======================================")
    menu = input("pilih menu : ")

    if menu == "1":
        akun = login()
        if akun:
            if akun[2] == "Albert Einstein Liem":
                menu_admin()
            else:
                menu_user(akun[0])
    elif menu == "2":
        register()
    elif menu == "3":
        clear()
        print("Terimakasih! Semoga beruntung!!")
        break
    else:
        print("Pilihan tidak valid")
        pause()
