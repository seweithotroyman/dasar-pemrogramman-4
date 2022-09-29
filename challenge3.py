import os
import sys
import numpy as np


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print("=== Aplikasi Operasi Matriks ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Keluar")
    pilihan = input("Pilih menu> ")
    return pilihan


def input_matriks():
    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))
    matriks = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            row.append(int(input(f"Masukkan nilai matriks ({i + 1}, {j + 1}): ")))
        matriks.append(row)
    return matriks


def penjumlahan():
    print("=== Penjumlahan Matriks ===")
    print("Matriks A")
    matriks_a = input_matriks()
    print("Matriks B")
    matriks_b = input_matriks()
    matriks_c = np.add(matriks_a, matriks_b)
    print("Hasil Penjumlahan")
    print(matriks_c)
    clear()
    return menu()


def pengurangan():
    print("=== Pengurangan Matriks ===")
    print("Matriks A")
    matriks_a = input_matriks()
    print("Matriks B")
    matriks_b = input_matriks()
    matriks_c = np.subtract(matriks_a, matriks_b)
    print("Hasil Pengurangan")
    print(matriks_c)
    clear()
    return menu()


def perkalian():
    print("=== Perkalian Matriks ===")
    print("Matriks A")
    matriks_a = input_matriks()
    print("Matriks B")
    matriks_b = input_matriks()
    matriks_c = np.dot(matriks_a, matriks_b)
    print("Hasil Perkalian")
    print(matriks_c)
    clear()
    return menu()


def main():
    while True:
        pilihan = menu()
        if pilihan == "1":
            penjumlahan()
        elif pilihan == "2":
            pengurangan()
        elif pilihan == "3":
            perkalian()
        elif pilihan == "4":
            sys.exit()
        else:
            print("Pilihan tidak tersedia")
            clear()
            continue


main()
