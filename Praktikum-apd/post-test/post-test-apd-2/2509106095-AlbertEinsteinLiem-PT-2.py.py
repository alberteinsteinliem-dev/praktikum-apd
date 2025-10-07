
nama = input("Masukkan nama lengkap: ")
nim = input("Masukkan NIM: ")

harga = int(input("Masukkan harga laptop: Rp "))

diskon_laptop = {
    "Acer": 5,
    "Asus": 7,
    "Lenovo": 10,
}
print("\n=== Hasil Perhitungan Diskon Laptop ===\n")
print(f"{nama} dengan NIM {nim} ingin membeli laptop seharga Rp {harga:,}")

print("\n{:<10} {:<10} {:<20}".format("Merek", "Diskon", "Harga Setelah Diskon"))
print("-" * 45)

for merek, persen in diskon_laptop.items():
    potongan = harga * (persen / 100)
    harga_akhir = harga - potongan
    print(f"{merek:<10} {persen:<2}%         Rp {harga_akhir:,.0f}")
print("-" * 45)