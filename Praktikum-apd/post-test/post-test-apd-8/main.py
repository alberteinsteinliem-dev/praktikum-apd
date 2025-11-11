from data import user, garis, pause
from admin import menu_admin
from user import menu_user

def register():
    print("=== REGISTER AKUN BARU ===")
    nama = input("Masukkan username baru: ")
    pw = input("Masukkan password baru: ")
    try:
        if nama not in user:
            user[nama] = {"password": pw, "role": "user"}
            print("Akun berhasil dibuat")
        else:
            print("Username sudah digunakan.")
    except ValueError:
        print("Terjadi kesalahan saat registrasi.")
    pause()

def login():
    nama = input("Username: ")
    pw = input("Password: ")
    try:
        if nama in user and user[nama]["password"] == pw:
            if user[nama]["role"] == "admin":
                menu_admin()
            else:
                menu_user(nama)
        else:
            print("Login gagal! Username atau password salah.")
    except ValueError:
        print("Terjadi kesalahan saat login.")
    pause()

def menu_utama():
    while True:
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
            break
        else:
            print("Pilihan tidak valid!")
            pause()

if __name__ == "__main__":
    menu_utama()