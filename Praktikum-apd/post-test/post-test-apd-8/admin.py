from data import lomba, peserta, garis, pause, tampil_lomba

def tambah_lomba():
    print("=== TAMBAH LOMBA BARU ===")
    nama_lomba = input("Lomba: ")
    hari = input("Tanggal lomba: ")
    aturan = input("Aturan lomba: ")
    hadiah = input("Hadiah lomba: ")

    try:
        id_baru = len(lomba) + 1
        lomba[id_baru] = {
            "nama": nama_lomba,
            "tanggal": hari,
            "aturan": aturan,
            "hadiah": hadiah
        }
        print("Lomba berhasil ditambahkan!")
    except ValueError:
        print("Ada kesalahan ketika menambah lomba.")
    pause()

def hapus_lomba():
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

def ubah_lomba():
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
    if len(peserta) == 0:
        print("Belum ada peserta terdaftar.")
    else:
        from prettytable import PrettyTable
        tabel = PrettyTable()
        tabel.field_names = ["Nama Peserta", "Lomba yang Diikuti"]
        for p in peserta:
            tabel.add_row([p["nama"], p["lomba"]])
        print(tabel)
    pause()

def menu_admin():
    from user import menu_user  # untuk akses jika admin login
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

        if pilih == "1":
            tampil_lomba(lomba)
            pause()
        elif pilih == "2":
            tambah_lomba()
        elif pilih == "3":
            ubah_lomba()
        elif pilih == "4":
            hapus_lomba()
        elif pilih == "5":
            lihat_peserta()
        elif pilih == "6":
            break
        else:
            print("Pilihan tidak valid!")
            pause()