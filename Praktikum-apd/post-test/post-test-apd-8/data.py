from prettytable import PrettyTable

user = {
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
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Lomba", "Tanggal", "Aturan", "Hadiah"]
        for i, d in data_lomba.items():
            tabel.add_row([i, d["nama"], d["tanggal"], d["aturan"], d["hadiah"]])
        print(tabel)