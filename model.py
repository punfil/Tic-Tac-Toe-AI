from keras.layers import Dense
from keras.layers import Dropout
from keras.models import Sequential
from keras.utils import to_categorical
import numpy as np

import constants


class TicTacToeModel:

    def __init__(self, numberOfInputs, numberOfOutputs, epochs, batchSize):
        self.epochs = epochs
        self.batchSize = batchSize
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.model = Sequential()

        #self.model.add(Dense(64, activation='relu', input_shape=(numberOfInputs, )))
        #self.model.add(Dense(128, activation='relu'))
       # self.model.add(Dense(128, activation='relu'))
        #self.model.add(Dense(128, activation='relu'))

        #Dalej zrobic zeby na 100 epokach i zwiekszyc jeszcze te neurony
        if constants.board_width == 5:
            # self.epochs = 100
            # self.model.add(Dense(64, activation='relu', input_shape=(numberOfInputs, )))
            # self.model.add(Dense(128, activation='relu'))
            # self.model.add(Dense(128, activation='relu'))
            # self.model.add(Dense(128, activation='relu'))
            # self.model.add(Dense(128, activation='relu'))
            # self.model.add(Dense(128, activation='relu'))
            self.epochs = 20
            self.model.add(Dense(512, activation='relu', input_shape=(numberOfInputs,)))
            self.model.add(Dense(512, activation='relu'))
            self.model.add(Dense(512, activation='relu'))
            self.model.add(Dense(256, activation='relu'))
            #self.model.add(Dense(64, activation='relu'))

        else:
            self.model.add(Dense(64, activation='relu', input_shape=(numberOfInputs,)))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dense(128, activation='relu'))
            self.model.add(Dense(128, activation='relu'))

        self.model.add(Dense(numberOfOutputs, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    def train(self, dataset):
        input = []
        output = []
        for data in dataset:
            input.append(data[1])
            output.append(data[0])

        X = np.array(input).reshape((-1, self.numberOfInputs))
        y = to_categorical(output, num_classes=3)
        # Train and test data split
        boundary = int(0.8 * len(X))
        X_train = X[:boundary]
        X_test = X[boundary:]
        y_train = y[:boundary]
        y_test = y[boundary:]
        self.model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=self.epochs, batch_size=self.batchSize)

    def predict(self, data, index):
        return self.model.predict(np.array(data).reshape(-1, self.numberOfInputs))[0][index]

    def save(self):
        """Save new model (previous is overwritten!!!)"""
        self.model.save_weights('./checkpoints/my_checkpoint')
        print("SAVED MODEL")
    def load(self):
        """Load last saved model"""
        self.model.load_weights('./checkpoints/my_checkpoint')
        print("LOADED MODEL")

    def save_best(self):
        """To save best model"""
        self.model.save_weights('./checkpoints/best_checkpoint_%i_size'%constants.board_width)
        print("SAVED BEST")

    def load_best(self):
        """To load actual the best model"""
        self.model.load_weights('./checkpoints/best_checkpoint_%i_size'%constants.board_width)
        print("LOADED BEST")