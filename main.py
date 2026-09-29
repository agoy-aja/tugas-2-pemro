npm = input('Masukkan NPM: ')
nama = input('Masukkan Nama: ')
umur = input('Masukkan Umur: ')
prodi = input('Masukkan Prodi: ')
tugas = float(input('Masukkan nilai Tugas: '))
uts = float(input('Masukkan nilai UTS: '))
uas = float(input('Masukkan nilai UAS: '))
nilaiakhir = (tugas + uts + uas) / 3

print('\n=== HASIL ===')
print('NPM         :', npm)
print('Nama        :', nama)
print('Umur        :', umur, 'tahun')
print('Prodi       :', prodi)
print('Tugas       :', tugas)
print('UTS         :', uts)
print('UAS         :', uas)
print('Nilai Akhir :', round(nilaiakhir, 2))

if nilaiakhir >= 75:
    print('Anda Lulus')
else:
    print('Anda Tidak Lulus')