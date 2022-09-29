import numpy as np
from sklearn.linear_model import LinearRegression

# x1 = baterai
# x2 = kamera
# y = harga

x1 = np.array([21, 16, 17, 20, 22, 18])
x2 = np.array([8, 2, 6, 4, 7, 3])
y = np.array([7, 3, 7, 2, 8, 3])

# hitung regresi linear berganda menggunakan scikit-learn
regresi = LinearRegression()
model = regresi.fit(np.column_stack([x1, x2]), y)

print("Persamaan regresi linear berganda menggunakan scikit-learn:")
# prediksi harga H4 dan H6
print("Prediksi harga H4 dengan rumus {} + {} * 14 + {} * 9 adalah {}".format(model.intercept_, model.coef_[0], model.coef_[1], model.intercept_ + model.coef_[0]*14 + model.coef_[1]*9))
print("Prediksi harga H6 dengan rumus {} + {} * 24 + {} * 5 adalah {}".format(model.intercept_, model.coef_[0], model.coef_[1], model.intercept_ + model.coef_[0]*24 + model.coef_[1]*5))