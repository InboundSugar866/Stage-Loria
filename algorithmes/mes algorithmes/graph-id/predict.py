# Import the required libraries
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['font.size'] = 10

# Load and preprocess the time series data
data = pd.read_csv("data/HDFS_1M.csv")
# Perform data preprocessing steps (e.g., handle missing values, normalization)

train_size = int(len(data) * 0.8)
data = list(data['event'])

# Split the data into training and testing sets

train_data, test_data = data[:train_size], data[train_size:]

# Prepare the input and output sequences
def create_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i+sequence_length])
        y.append(data[i+sequence_length])
    return np.array(X), np.array(y)

sequence_length = 20
X_train, y_train = create_sequences(train_data, sequence_length)
X_test, y_test = create_sequences(test_data, sequence_length)

# Build the LSTM model
model = Sequential()
model.add(LSTM(units=64, input_shape=(sequence_length, 1)))
model.add(Dense(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=20, batch_size=256)

# Predict on the test set
predictions = model.predict(X_test)

error_mse = mean_squared_error(
                y_true = y_test,
                y_pred = predictions
            )
print(f"Test error (MSE): {error_mse}") 
# 10epoch = 6.528650261525933 batch = 32 sequence = 10 adam
# 10epoch = 6.479395097692808 batch = 64 sequence = 20 adam

plt.figure(figsize=(14, 7))

plt.plot(range(len(train_data)), train_data, color='blue', label='Train Data')
plt.plot(range(len(train_data), len(train_data)+len(test_data)), test_data, color='red', label='Test Data')
plt.plot(range(len(train_data)+sequence_length, len(train_data)+sequence_length+len(predictions)), 
          np.round(predictions).astype(int), color='yellow', label='Predictions')

plt.xlabel('Time')
plt.ylabel('Event')
plt.legend()
plt.show()