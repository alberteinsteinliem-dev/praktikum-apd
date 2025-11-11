from data import lomba, peserta, garis, pause, tampil_lomba

def daftar_lomba(nama):
    tampil_lomba(lomba)
    nomor = input("Pilih nomor lomba: ")
    try:
        nomor = int(nomor)
        if nomor in lomba:
            peserta.append({"nama": nama, "lomba": lomba[nomor]["nama"]})
            print("Berhasil terdaftar.")
        else:
            print("Nomor lomba tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")
    pause()

def lihat_lomba_diikuti(nama):
    ada = False
    for p in peserta:
        if p["nama"] == nama:
            print("-", p["lomba"])
            ada = True
    if not ada:
        print("Belum ikut lomba apa pun.")
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