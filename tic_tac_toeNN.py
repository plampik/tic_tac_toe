import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tic_tac_toe1 import state_field

model = keras.Sequential([
    layers.Flatten(input_shape=(3, 3)),
    layers.Dense(128, activation='relu'),
    layers.Dense(9, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

global predicted
def change_predicted(state_field):

    predicted = model.predict(np.array([state_field]))

next_move = np.argmax(predicted)

next_move_row = next_move //3
next_move_col = next_move %3
def next_row():
    return next_move_row
def next_col():
    return next_move_col