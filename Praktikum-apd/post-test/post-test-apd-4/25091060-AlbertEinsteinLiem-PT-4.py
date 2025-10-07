# Pembelian Tiket Bioskop 

nama = "Albert Einstein Liem"
NIM = "2509106095"

harga_reguler = 50000
harga_vip = 100000
harga_vvip = 150000

percobaan = 0
maks_percobaan = 3
login_berhasil = False

while percobaan < maks_percobaan:
    print("== SELAMAT DATANG DI BIOSKOP SCP ==")
    username = input("Username: ")
    password = input("Password: ")

    if username == nama and password == NIM:
        print("Login berhasil! Selamat datang,", username, "silahkan pilih tiket anda!")
        login_berhasil = True
        break
    else:
        percobaan += 1
        print("Login gagal! nama dan NIM anda tidak sesuai, percobaan ke -", percobaan)
        if percobaan == maks_percobaan:
            print("Percobaan habis! silahkan coba beberapa saat lagi!")
            exit()

while login_berhasil:
    print("=== MENU PEMBELIAN TIKET BIOSKOP MALL SCP ===")
    print("1. Tiket Reguler  : Rp 50.000")
    print("2. Tiket VIP      : Rp 100.000")
    print("3. Tiket VVIP     : Rp 150.000")
    print("4. Keluar")

    pilihan = input("Pilih jenis tiket (1-4): ")

    if pilihan == "1":
        Kategori = "Reguler"
        harga = harga_reguler
    elif pilihan == "2":
        Kategori = "VIP"
        harga = harga_vip
    elif pilihan == "3":
        Kategori = "VVIP"
        harga = harga_vvip
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan ulangi lagi")
        continue

    jumlah_str = input("Jumlah tiket: ")

    if jumlah_str == "":
        print("Input tidak boleh kosong.")
        continue

    hanya_angka = True
    for a in jumlah_str:
        if a < '0' or a > '9':
            hanya_angka = False
        break

    if hanya_angka == False:
        print("Input harus berupa angka.")
        continue

    jumlah = int(jumlah_str)
    if jumlah <= 0:
        print("Jumlah tiket wajib lebih dani 0")
        continue

    total = 0
    for i in range(jumlah):
        total += harga

    if total >= 300000:
        potongan = total * 0.12
        total_bayar = total - potongan
        bonus = f"Diskon 12% (Rp {int(potongan)})"
    elif total >= 200000:
        potongan = total * 0.08
        total_bayar = total - potongan
        bonus = f"Diskon 8% (Rp {int(potongan)})"
    elif total >= 150000:
        potongan = 0
        total_bayar = total
        bonus = "Bonus Poster Film Eksklusif"
    else:
        potongan = 0
        total_bayar = total
        bonus = "Tidak ada bonus/diskon"

    print("")
    print("=== HASIL PEMBELIAN TIKET ANDA ===")
    print("Jenis Tiket :", Kategori)
    print("Jumlah Tiket:", jumlah)
    print("Total Harga :", f"Rp {total:,}")
    print("Bonus/Promo :", bonus)
    print("Total bayar anda :", f"Rp {int(total_bayar):,}")