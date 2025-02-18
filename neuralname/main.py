import random
import numpy as np
import tensorflow as tf



from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Activation
from tensorflow.keras.optimizers import RMSprop

# Suppress TensorFlow logging 
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Download Shakespeare text dataset
filepath = tf.keras.utils.get_file(
    'shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt'
)

# Read and preprocess text
text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()
text = text[:500000] 

# Create character mappings
characters = sorted(set(text))
char_to_index = {c: i for i, c in enumerate(characters)}
index_to_char = {i: c for i, c in enumerate(characters)}

# Define sequence parameters
SEQ_LENGTH = 40
STEP_SIZE = 3

'''
# Prepare training data
sentences = []
next_characters = []

for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i:i + SEQ_LENGTH])
    next_characters.append(text[i + SEQ_LENGTH])

# Initialize one-hot encoded arrays
x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype=bool)
y = np.zeros((len(sentences), len(characters)), dtype=bool)

# Convert text to one-hot encoding
for i, sentence in enumerate(sentences):
    for t, character in enumerate(sentence):
        x[i, t, char_to_index[character]] = 1
    y[i, char_to_index[next_characters[i]]] = 1
'''
# Load the trained model
model = tf.keras.models.load_model('textgenerator.keras')

print("Model loaded successfully!")



def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def generate_text(length, temperature):
    start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
    generated = ''
    sentence = text[start_index: start_index + SEQ_LENGTH]
    generated += sentence
    for i in range(length):
        x_predictions = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, char in enumerate(sentence):
            x_predictions[0, t, char_to_index[char]] = 1

        predictions = model.predict(x_predictions, verbose=0)[0]
        next_index = sample(predictions,
                                 temperature)
        next_character = index_to_char[next_index]

        generated += next_character
        sentence = sentence[1:] + next_character
    return generated

print(generate_text(300, 0.2))
print(generate_text(300, 0.4))
print(generate_text(300, 0.5))
print(generate_text(300, 0.6))
print(generate_text(300, 0.7))
print(generate_text(300, 0.8))




# Build the LSTM model
#model = Sequential()
#model.add(LSTM(128, input_shape=(SEQ_LENGTH, len(characters))))
#model.add(Dense(len(characters)))
#model.add(Activation('softmax'))

# Compile the model
#model.compile(loss='categorical_crossentropy', optimizer=RMSprop(learning_rate=0.01))

# Train the model
#print("Training model...")
#model.fit(x, y, batch_size=256, epochs=4)

# Save the trained model
#model.save('textgenerator.keras')
#print("Model saved successfully!")

