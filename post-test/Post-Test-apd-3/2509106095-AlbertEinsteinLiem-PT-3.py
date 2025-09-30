nama_pengguna="Albert Einstein Liem"
NIM_pengguna='2509106095'
biaya_langganan_perbulan = 1500000

print("====login akun====")
nama = input("nama lengkap anda :")
nim = input("NIM anda :")

if nama==nama_pengguna and nim==NIM_pengguna:

    print("==============================")
    print("selamat datang " + nama_pengguna)
    print("==============================")
    print("Silahkan pilih paket langganan anda")
    print("==============================")
    print("1. paket Bronze = akses dasar ke lagu-lagu populer.")
    print("(Biaya admin 1%)")
    print("")
    print("2. paket Silver = akses lagu premium dan playlist kustom.")
    print("(biaya admin 3%)")
    print("")
    print("3. paket Gold = akses lagu premium, playlist kustom, dan mode offline.")
    print("(biaya admin 5%)")
    print("")
    print("4. paket Platinum = akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis.")
    print("(biaya admin 7%)")

    pilihan = input ("pilih paket anda :")
    
    if pilihan == "1":
            admin = 0.01
            paket = "Bronze"
    elif pilihan == "2":
            admin = 0.03
            paket = "Silver"
    elif pilihan == "3":
            admin = 0.05
            paket = "Gold"
    elif pilihan == "4":
            admin = 0.07
            paket = "Platinum"
    else:
        print("tidak valid")
        exit ()

    total = biaya_langganan_perbulan + (biaya_langganan_perbulan * admin)
    print("===============================")
    print("pembayaran anda")
    print("==============================")
    print("paket :", paket)
    print("biaya bulanan : Rp", biaya_langganan_perbulan)
    print("Biaya admin :", int(admin*100),"%")
    print("total bayaran : Rp", int(total))
    print("Terimakasih telah berlangganan")

else:
     print ('==============================')
     print ('gagal masuk akun')