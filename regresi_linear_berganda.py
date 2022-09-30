import numpy as np
from sklearn.linear_model import LinearRegression

# data training
x1 = np.array([21, 16, 17, 20, 22, 18])
x2 = np.array([8, 2, 6, 4, 7, 3])
y = np.array([7, 3, 7, 2, 8, 3])

# hitung regresi linear berganda menggunakan scikit-learn
regresi = LinearRegression()
model = regresi.fit(np.column_stack((x1, x2)), y)

# tampilkan lengkap dari mencari semua sigma
print("Persamaan regresi linear berganda manual:")
print("sigma_x1 = ", np.sum(x1))
print("sigma_x2 = ", np.sum(x2))
print("sigma_y = ", np.sum(y))
print("sigma_x1_squared = ", np.sum(x1**2))
print("sigma_x2_squared = ", np.sum(x2**2))
print("sigma_x1x2 = ", np.sum(x1*x2))
print("sigma_x1y = ", np.sum(x1*y))
print("sigma_x2y = ", np.sum(x2*y))

sigma_x1_2 = np.sum(x1**2) - (np.sum(x1)**2 / len(x1))
sigma_x2_2 = np.sum(x2**2) - (np.sum(x2)**2 / len(x2))
sigma_y_2 = np.sum(y**2) - (np.sum(y)**2 / len(y))
sigma_x1_y = np.sum(x1*y) - (np.sum(x1)*np.sum(y)) / len(y)
sigma_x2_y = np.sum(x2*y) - (np.sum(x2)*np.sum(y)) / len(y)
sigma_x1_x2 = np.sum(x1*x2) - (np.sum(x1)*np.sum(x2)) / len(y)

# hitung a, b1, b2 data
b1 = (sigma_x2_2*sigma_x1_y - sigma_x2_y*sigma_x1_x2) / (sigma_x1_2*sigma_x2_2 - sigma_x1_x2**2)
b2 = (sigma_x1_2*sigma_x2_y - sigma_x1_y*sigma_x1_x2) / (sigma_x1_2*sigma_x2_2 - sigma_x1_x2**2)
a = (np.sum(y) - (b1*np.sum(x1)) - (b2*np.sum(x2))) / len(y)

# prediksi harga H4 dan H6
print("Prediksi harga H4 dengan rumus {} + {} * 14 + {} * 9 adalah {}".format(a, b1, b2, a + b1*14 + b2*9))
print("Prediksi harga H6 dengan rumus {} + {} * 24 + {} * 5 adalah {}".format(a, b1, b2, a + b1*24 + b2*5))

print()
print("Persamaan regresi linear berganda menggunakan scikit-learn:")
# prediksi harga H4 dan H6
print("Prediksi harga H4 dengan rumus {} + {} * 14 + {} * 9 adalah {}".format(model.intercept_, model.coef_[0], model.coef_[1], model.intercept_ + model.coef_[0]*14 + model.coef_[1]*9))
print("Prediksi harga H6 dengan rumus {} + {} * 24 + {} * 5 adalah {}".format(model.intercept_, model.coef_[0], model.coef_[1], model.intercept_ + model.coef_[0]*24 + model.coef_[1]*5))
