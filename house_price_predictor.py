from sklearn.linear_model import LinearRegression
import numpy as np

house_size = np.array([[500], [800], [1000], [1200], [1500]])
price = np.array([100000, 150000, 200000, 230000, 300000])

model = LinearRegression()
model.fit(house_size, price)

size = int(input("Enter house size: "))

prediction = model.predict([[size]])

print("Predicted Price:", prediction[0])