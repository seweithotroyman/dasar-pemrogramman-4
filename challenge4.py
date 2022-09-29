import numpy as np


# buat fungsi linear regresi
def linear_regression(x, y, x_prediksi):
    # jumlah data
    jumlah_data = np.size(x)

    # rata-rata x dan y
    rata_rata_x, rata_rata_y = np.mean(x), np.mean(y)

    # hitung sigma pembilang
    sigma_pembilang = 0
    sigma_penyebut = 0
    for i in range(jumlah_data):
        sigma_pembilang += x[i] * (y[i] - rata_rata_y)
        sigma_penyebut += x[i] * (x[i] - rata_rata_x)

    # hitung koefisien regresi
    koefisien_regresi = sigma_pembilang / sigma_penyebut

    # hitung intercept
    intercept = rata_rata_y - (koefisien_regresi * rata_rata_x)

    # hitung y_prediksi
    y_prediksi = intercept + (koefisien_regresi * x_prediksi)

    return koefisien_regresi, intercept, x_prediksi, y_prediksi


x = np.array([8, 2, 6, 4, 7, 3])
y = np.array([7, 3, 7, 2, 8, 3])

# prediksi nilai x = 9
x_prediksi = 9

# panggil fungsi linear regresi
prediksi_H4 = linear_regression(x, y, x_prediksi)

print("""
    Rumus Linear Regresi: y = {}x + {}
    Prediksi x = {}
    Prediksi y = {}
    """.format(prediksi_H4[0], prediksi_H4[1], prediksi_H4[2], prediksi_H4[3]))

# prediksi nilai x = 5
x_prediksi = 5

# panggil fungsi linear regresi
prediksi_H6 = linear_regression(x, y, x_prediksi)

print("""
    Rumus Linear Regresi: y = {}x + {}
    Prediksi x = {}
    Prediksi y = {}
    """.format(prediksi_H6[0], prediksi_H6[1], prediksi_H6[2], prediksi_H6[3]))
