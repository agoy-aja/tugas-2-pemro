from datetime import datetime

data_parkir = {}
riwayat_pembayaran = []

def input_waktu(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt), "%H:%M").time()
        except ValueError:
            print("Format waktu salah! Contoh: 08:30")

def tambah_kendaraan():
    print("\n=== PARKIR MASUK ===")
    plat = input("Masukkan plat nomor: ").upper()
    
    if plat in data_parkir:
        print("Kendaraan dengan plat tersebut sudah ada di dalam!")
        return

    while True:
        jenis = input("Jenis kendaraan (motor/mobil): ").lower()
        if jenis in ["motor", "mobil"]: break
        print("Jenis kendaraan tidak valid!")

    jam = input_waktu("Jam masuk (HH:MM): ")
    
    data_parkir[plat] = {"jenis": jenis, "jam_masuk": jam}
    print("Kendaraan berhasil masuk.")

def tampil_data():
    print("\n=== DATA KENDARAAN PARKIR ===")
    if not data_parkir:
        print("Parkiran kosong.")
        return
        
    for i, (plat, detail) in enumerate(data_parkir.items(), 1):
        print(f"{i}. Plat: {plat} | Jenis: {detail['jenis']} | Jam Masuk: {detail['jam_masuk']}")

def kendaraan_keluar():
    print("\n=== PARKIR KELUAR ===")
    if not data_parkir:
        print("Tidak ada kendaraan di parkiran."); return

    plat = input("Masukkan plat nomor: ").upper()
    if plat not in data_parkir:
        print("Plat nomor tidak ditemukan!"); return

    jam_keluar = input_waktu("Jam keluar (HH:MM): ")
    detail = data_parkir[plat]
    
    masuk = datetime.combine(datetime.today(), detail["jam_masuk"])
    keluar = datetime.combine(datetime.today(), jam_keluar)
    
    durasi = (keluar - masuk).seconds // 3600
    if durasi < 1: durasi = 1

    tarif = 3000 if detail["jenis"] == "motor" else 5000
    biaya = durasi * tarif

    print(f"\n=== DETAIL PARKIR ===\nPlat Nomor : {plat}\nJenis      : {detail['jenis']}")
    print(f"Jam Masuk  : {detail['jam_masuk']}\nJam Keluar : {jam_keluar}")
    print(f"Durasi     : {durasi} jam\nBiaya      : Rp {biaya}")

    print("\n=== PEMBAYARAN ===")
    while True:
        try:
            bayar = int(input("Masukkan uang pembayaran: Rp "))
            if bayar >= biaya:
                print(f"\n=== PEMBAYARAN BERHASIL ===\nTotal Bayar : Rp {biaya}")
                print(f"Uang Masuk  : Rp {bayar}\nKembalian   : Rp {bayar - biaya}")
                riwayat_pembayaran.append(biaya)
                break
            print("Uang tidak cukup!")
        except ValueError:
            print("Input harus berupa angka!")

    del data_parkir[plat]

def tampil_riwayat():
    print("\n=== RIWAYAT PEMBAYARAN ===")
    if not riwayat_pembayaran:
        print("Belum ada transaksi."); return

    for i, nominal in enumerate(riwayat_pembayaran, 1):
        print(f"{i}. Rp {nominal}")
    print(f"----------------------\nTotal Pendapatan: Rp {sum(riwayat_pembayaran)}")

menu_aksi = {
    "1": tambah_kendaraan,
    "2": kendaraan_keluar,
    "3": tampil_data,
    "4": lambda: print(f"\n=== INFORMASI PARKIR ===\nJumlah kendaraan saat ini: {len(data_parkir)}"),
    "5": tampil_riwayat
}

while True:
    print("\n=================================\n SISTEM PENGELOLAAN LAHAN PARKIR \n=================================")
    print("1. Kendaraan Masuk\n2. Kendaraan Keluar\n3. Tampilkan Data Parkir\n4. Total Kendaraan\n5. Riwayat Pembayaran\n6. Keluar")
    
    pilihan = input("Pilih menu: ")
    if pilihan in menu_aksi:
        menu_aksi[pilihan]()
    elif pilihan == "6":
        print("\nProgram selesai."); break
    else:
        print("Menu tidak valid!")