from prettytable import PrettyTable

mahasiswa = []


def tambah_mahasiswa(nim, nama, email):
    mahasiswa_baru = {
        "nim": nim,
        "nama": nama,
        "email": email
    }
    mahasiswa.append(mahasiswa_baru)


def cari_mahasiswa(nim):
    for mhs in mahasiswa:
        if mhs["nim"] == nim:
            return mhs
    return None


def edit_mahasiswa(nim, nama, email):
    for mhs in mahasiswa:
        if mhs["nim"] == nim:
            mhs["nama"] = nama
            mhs["email"] = email
            return True
    return None


def hapus_mahasiswa(nim):
    for mhs in mahasiswa:
        if mhs["nim"] == nim:
            mahasiswa.remove(mhs)
            return True
    return False


# tampilkan data mahasiswa menggunakan prettytables
def tampilkan_mahasiswa():
    table = PrettyTable()
    table.field_names = ["NIM", "Nama", "Email"]
    for mhs in mahasiswa:
        table.add_row([mhs["nim"], mhs["nama"], mhs["email"]])
    print(table)


def main():
    while True:
        print("=== Aplikasi Data Mahasiswa ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Tampilkan Data Mahasiswa")
        print("4. Edit Data Mahasiswa")
        print("5. Hapus Data Mahasiswa")
        print("6. Keluar")
        pilihan = input("Pilih menu> ")

        # clear screen
        print("\n" * 100)

        if pilihan == "1":
            print("=== Tambah Data Mahasiswa ===")
            nim = input("NIM: ")
            nama = input("Nama: ")
            email = input("Email: ")
            tambah_mahasiswa(nim, nama, email)
        elif pilihan == "2":
            print("=== Cari Data Mahasiswa ===")
            nim = input("NIM: ")
            mhs = cari_mahasiswa(nim)
            if mhs is not None:
                print("Data mahasiswa:")
                print("NIM: ", mhs["nim"])
                print("Nama: ", mhs["nama"])
                print("Email: ", mhs["email"])
            else:
                print("Data mahasiswa tidak ditemukan")
        elif pilihan == "3":
            print("=== Tampilkan Data Mahasiswa ===")
            tampilkan_mahasiswa()
        elif pilihan == "4":
            print("=== Edit Data Mahasiswa ===")
            nim = input("NIM : ")
            cari_data = cari_mahasiswa(nim)
            if cari_data:
                nama = input("Input nama baru : ")
                email = input("Input email baru: ")
                if edit_mahasiswa(nim, nama, email):
                    print("Data berhasil diubah")
                    # print(mahasiswa)
        elif pilihan == "5":
            print("=== Hapus Data Mahasiswa ===")
            nim = input("NIM : ")
            if hapus_mahasiswa(nim):
                print("Data berhasil dihapus")
            else:
                print("Data tidak ditemukan")
        elif pilihan == "6":
            break
        else:
            print("Menu tidak tersedia")


if __name__ == "__main__":
    main()
