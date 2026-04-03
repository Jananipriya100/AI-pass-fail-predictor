from sklearn.linear_model import LogisticRegression
import numpy as np
import joblib

X = np.array([[30], [40], [50], [60], [70], [80]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")
