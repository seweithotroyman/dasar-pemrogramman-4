### DASAR PEMROGRAMAN JOB SHEET 4: LIST DAN TUPLE
<p align="center">
    <img src="https://github.com/ardzz/dasar-pemrogaman-2/raw/master/images/logo-polines.png" alt="Logo Polines" width="300" height="300">
</p>

#### Dibuat dan disusun oleh
| Variabel | Nilai               |
|----------|---------------------|
| Nama     | Naufal Reky Ardhana |
| NIM      | 4.33.22.0.21        |
| Kelas    | TI-1A               |

**PROGRAM STUDI TEKNIK INFORMATIKA JURUSAN TEKNIK ELEKTRO POLITEKNIK NEGERI SEMARANG - 2022**

#### Daftar Isi

#### BAB I. Landasan Teori
Di dalam bahasa pemrograman Python, terdapat dua tipe data yang dapat digunakan untuk menyimpan kumpulan data, yaitu list dan tuple. Keduanya dapat menyimpan kumpulan data, baik itu berupa angka, string, maupun tipe data lainnya. Perbedaan utama dari kedua tipe data tersebut adalah list bersifat mutable, sedangkan tuple bersifat immutable. Dalam bab ini, akan dibahas mengenai list dan tuple, serta perbedaan dan kegunaan dari kedua tipe data tersebut.

#### BAB II. List
List adalah salah satu tipe data yang dapat digunakan untuk menyimpan kumpulan data. List bersifat mutable, artinya data yang disimpan dalam list dapat diubah. List dapat menyimpan data dengan tipe data yang berbeda, baik itu angka, string, maupun tipe data lainnya. List dapat dibuat dengan cara menuliskan data yang akan disimpan dalam list, dipisahkan dengan koma, di dalam tanda kurung siku. Contoh:
```python
list = [1, 2, 3, 4, 5]
```
Sifat dari nilai List (item) yaitu terurut (ordered), dapat diubah (changeable), dan membolehkan nilai yang sama (duplicate). Data dari list diurutkan dalam bentuk indeks mulai dari [0], [1], dan seterusnya. Item dari List mempunyai urutan tertentu dan tidak berubah, jika terdapat item baru maka item tersebut ditempatkan pada urutan terakhir. Item dari List dapat diubah dengan cara ditambah dan dihapus setelah dibuat

#### BAB III. Tuple
Tuple adalah salah satu tipe data yang dapat digunakan untuk menyimpan kumpulan data. Tuple bersifat immutable, artinya data yang disimpan dalam tuple tidak dapat diubah. Tuple dapat menyimpan data dengan tipe data yang berbeda, baik itu angka, string, maupun tipe data lainnya. Tuple dapat dibuat dengan cara menuliskan data yang akan disimpan dalam tuple, dipisahkan dengan koma, di dalam tanda kurung biasa. Contoh:
```python
tuple = (1, 2, 3, 4, 5)
```
Sifat dari nilai Tuple (item) yaitu terurut (ordered), tidak dapat diubah (unchangeable), dan membolehkan nilai yang sama (duplicate). Data dari tuple diurutkan dalam bentuk indeks mulai dari [0], [1], dan seterusnya. Item dari Tuple mempunyai urutan tertentu dan tidak berubah, jika terdapat item baru maka item tersebut ditempatkan pada urutan terakhir. Item dari Tuple tidak dapat diubah dengan cara ditambah dan dihapus setelah dibuat

#### BAB IV. Kegunaan List dan Tuple
List dan tuple memiliki kegunaan yang berbeda. List bersifat mutable, artinya data yang disimpan dalam list dapat diubah. Sedangkan tuple bersifat immutable, artinya data yang disimpan dalam tuple tidak dapat diubah. Kegunaan dari list adalah untuk menyimpan data yang dapat diubah, seperti data yang akan diubah oleh pengguna. Sedangkan tuple digunakan untuk menyimpan data yang tidak dapat diubah, seperti data yang tidak akan diubah oleh pengguna.

#### BAB V. Praktikum
##### Alat dan Bahan
- Laptop
- Python `3.10.0`
- PyCharm `2021.2.3`
- Git `2.33.0`

##### Langkah Kerja
Sebuah projek aplikasi dibangun menggunakan pemrograman Python. Aplikasi ini dapat menyimpan dan mencari data mahasiswa berupa NIM, Nama, dan Email. Objek yang digunakan untuk menampung data adalah List. Aplikasi juga dapat menampilkan semua data.

1. Buat sebuah projek baru dengan nama `job-sheet-4` menggunakan PyCharm.
2. Buat sebuah file dengan nama `main.py` di dalam projek tersebut.
3. Buat sebuah list kosong dengan nama `mahasiswa`.
4. Buat sebuah fungsi dengan nama `tambah_mahasiswa` yang menerima parameter `nim`, `nama`, dan `email`. Fungsi ini akan menambahkan data mahasiswa ke dalam list `mahasiswa`.
5. Buat sebuah fungsi dengan nama `cari_mahasiswa` yang menerima parameter `nim`. Fungsi ini akan mencari data mahasiswa berdasarkan NIM yang dimasukkan oleh pengguna. Jika data ditemukan, maka fungsi ini akan mengembalikan data mahasiswa tersebut. Jika data tidak ditemukan, maka fungsi ini akan mengembalikan `None`.
6. Buat sebuah fungsi dengan nama `tampilkan_mahasiswa` yang tidak menerima parameter.
7. Buat sebuah fungsi dengan nama `main` yang tidak menerima parameter.
8. Di dalam fungsi `main`, buat sebuah perulangan `while` yang akan berjalan selama `True`.
9. Di dalam perulangan `while`, tampilkan menu aplikasi.
10. Di dalam perulangan `while`, minta pengguna untuk memasukkan pilihan menu.
11. Di dalam perulangan `while`, jika pengguna memilih menu `1`, maka minta pengguna untuk memasukkan NIM, Nama, dan Email.
12. Di dalam perulangan `while`, jika pengguna memilih menu `1`, maka panggil fungsi `tambah_mahasiswa` dengan parameter NIM, Nama, dan Email yang dimasukkan oleh pengguna.
13. Di dalam perulangan `while`, jika pengguna memilih menu `2`, maka minta pengguna untuk memasukkan NIM.
14. Di dalam perulangan `while`, jika pengguna memilih menu `2`, maka panggil fungsi `cari_mahasiswa` dengan parameter NIM yang dimasukkan oleh pengguna.
15. Di dalam perulangan `while`, jika pengguna memilih menu `2`, maka tampilkan data mahasiswa yang dikembalikan oleh fungsi `cari_mahasiswa`.
16. Di dalam perulangan `while`, jika pengguna memilih menu `3`, maka panggil fungsi `tampilkan_mahasiswa`.
17. Di dalam perulangan `while`, jika pengguna memilih menu `4`, maka keluar dari perulangan `while`.

```python
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
```

