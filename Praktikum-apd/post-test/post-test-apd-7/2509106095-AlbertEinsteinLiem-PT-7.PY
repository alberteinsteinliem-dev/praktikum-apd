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

def garis():
    print("=======================================")

def pause():
    input("Pencet enter untuk lanjut...")

def tampil_lomba(data_lomba):
    if len(data_lomba) == 0:
        print("Belum ada lomba terdaftar.")
    else:
        for i, d in data_lomba.items():
            print(f"{i}. {d['nama']}")
            print(f"   Tanggal  : {d['tanggal']}")
            print(f"   Peraturan: {d['aturan']}")
            print(f"   Hadiah   : {d['hadiah']}")
            print()

def valid_angka(teks):
    try:
        int(teks)
        return True
    except ValueError:
        return False

def tambah_lomba():
    global lomba
    print("=== TAMBAH LOMBA BARU ===")
    nama_lomba = input("Lomba: ")
    hari = input("Tanggal lomba: ")
    aturan = input("Aturan lomba: ")
    hadiah = input("Hadiah lomba: ")

    try:
        id_baru = len(lomba) + 1
        lomba[id_baru] = {}
        lomba[id_baru]["nama"] = nama_lomba
        lomba[id_baru]["tanggal"] = hari
        lomba[id_baru]["aturan"] = aturan
        lomba[id_baru]["hadiah"] = hadiah
        print("Lomba berhasil ditambahkan!")
    except ValueError:
        print("Ada kesalahan ketika menambah lomba.")
    pause()

def hapus_lomba():
    global lomba
    print("=== HAPUS LOMBA ===")
    tampil_lomba(lomba)
    nomor = input("Nomor lomba yang ingin anda hapus: ")
    try:
        nomor = int(nomor)
        if nomor in lomba:
            del lomba[nomor]
            print("Lomba berhasil dihapus!")
        else:
            print("Nomor lomba tidak ditemukan.")
    except ValueError:
        print("Input tidak valid, masukkan angka yang benar.")
    pause()

def menu_utama():
    garis()
    print("=== DAFTAR LOMBA TAHUN BARU ===")
    garis()
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    garis()
    menu = input("Pilih menu: ")

    if menu == "1":
        login()
    elif menu == "2":
        register()
    elif menu == "3":
        print("Terima kasih! Semoga beruntung!!")
        return
    else:
        print("Pilihan tidak valid!")
        pause()
    menu_utama()

def login():
    global users
    nama = input("Username: ")
    pw = input("Password: ")

    try:
        if nama in users and users[nama]["password"] == pw:
            role = users[nama]["role"]
            if role == "admin":
                menu_admin()
            else:
                menu_user(nama)
        else:
            print("Login gagal! Username atau password salah.")
    except ValueError:
        print("Terjadi kesalahan saat login.")
    pause()

def register():
    global users
    print("=== REGISTER AKUN BARU ===")
    nama = input("Masukkan username baru: ")
    pw = input("Masukkan password baru: ")

    try:
        if nama not in users:
            akun_baru = {"password": pw, "role": "user"}
            users[nama] = akun_baru
            print("Akun berhasil dibuat")
        else:
            print("Username sudah digunakan.")
    except ValueError:
        print("Terjadi kesalahan saat registrasi.")
    pause()

def menu_admin():
    while True:
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

        lokal_pilihan = pilih

        if lokal_pilihan == "1":
            tampil_lomba(lomba)
            pause()
        elif lokal_pilihan == "2":
            tambah_lomba()
        elif lokal_pilihan == "3":
            ubah_lomba()
        elif lokal_pilihan == "4":
            hapus_lomba()
        elif lokal_pilihan == "5":
            lihat_peserta()
        elif lokal_pilihan == "6":
            break
        else:
            print("Pilihan tidak valid!")
            pause()

def ubah_lomba():
    global lomba
    tampil_lomba(lomba)
    nomor = input("Nomor lomba yang ingin anda ubah diubah: ")
    try:
        nomor = int(nomor)
        if nomor in lomba:
            print("Masukkan data baru:")
            nama_baru = input("Nama: ")
            tanggal_baru = input("Tanggal: ")
            aturan_baru = input("Peraturan: ")
            hadiah_baru = input("Hadiah: ")

            if nama_baru:
                lomba[nomor]["nama"] = nama_baru
            if tanggal_baru:
                lomba[nomor]["tanggal"] = tanggal_baru
            if aturan_baru:
                lomba[nomor]["aturan"] = aturan_baru
            if hadiah_baru:
                lomba[nomor]["hadiah"] = hadiah_baru

            print("Data lomba berhasil diubah!")
        else:
            print("Nomor lomba tidak valid.")
    except ValueError:
        print("Input tidak valid, harus angka.")
    pause()

def lihat_peserta():
    try:
        if len(peserta) == 0:
            print("Belum ada peserta terdaftar.")
        else:
            for p in peserta:
                print("Nama Peserta :", p["nama"])
                print("Mengikuti    :", p["lomba"])
                print()
    except ValueError:
        print("Ada kesalahan saat menampilkan peserta")
    pause()

def menu_user(nama):
    while True:
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
            tampil_lomba(lomba)
            pause()
        elif pilih == "2":
            daftar_lomba(nama)
        elif pilih == "3":
            lihat_lomba_diikuti(nama)
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid!")
            pause()

def daftar_lomba(nama):
    global peserta
    tampil_lomba(lomba)
    nomor = input("Pilih nomor lomba: ")
    try:
        nomor = int(nomor)
        if nomor in lomba:
            data_baru = {"nama": nama, "lomba": lomba[nomor]["nama"]}
            peserta.append(data_baru)
            print("Berhasil terdaftar.")
        else:
            print("Nomor lomba tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")
    pause()

def lihat_lomba_diikuti(nama):
    try:
        ada = False
        for p in peserta:
            if p["nama"] == nama:
                print("-", p["lomba"])
                ada = True
        if not ada:
            print("Belum ikut lomba apa pun.")
    except ValueError:
        print("Terjadi kesalahan saat melihat lomba.")
    pause()

menu_utama()