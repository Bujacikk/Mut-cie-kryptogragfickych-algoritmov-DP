import numpy as np
from sklearn.linear_model import LinearRegression

# Předchozí hodnoty
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Příslušné hodnoty
y = np.array([0.02, 1.62, 107.16, 6966.77, 509956.14293768])

# Transformace dat na exponenciální škálu
y_exp = np.log(y)

# Inicializace a natrénování exponenciální regrese
regression = LinearRegression()
regression.fit(X, y_exp)

# Predikce 5. hodnoty
prediction_exp = regression.predict([[6]])

# Převod předpovědi zpět na lineární škálu
prediction = np.exp(prediction_exp)

print(prediction)