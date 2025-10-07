for i in range (1, 10, 3):
    print(f'perulangan ke {i}')

simpan = [1, 'adri', 4.00, True]
for i in simpan:
    print(i)

for i in 'adrii':
    print (i)

for i in range(10):
    for j in range (0, i+1):
        print('#', end='')
        print('')

while True:
    print('ulangi')

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input('ulang lagi ? ')
print(f'total perulangan: {hitung}')

angka = [20]
print('mencari angka pertama yang lebih dari 10...')
for n in angka:
    print(f'sekarang memeriksa angka: {n}')
    if n>10:
        print(f'angka {n} lebih besar dari 10, perulangan berhenti.')
        break
print('progam selesai')

for i in range(1, 11):
    if i % 2 !=0:
        continue
    print(f'angka genap ditemukan: {i}')
    print('gaada')
