import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from music21 import stream, note

# Sample music notes dataset
notes = [60, 62, 64, 65, 67, 69, 71, 72,
         72, 71, 69, 67, 65, 64, 62, 60]

# Prepare data
sequence_length = 4
X = []
y = []

for i in range(len(notes) - sequence_length):
    X.append(notes[i:i + sequence_length])
    y.append(notes[i + sequence_length])

X = np.array(X)
y = np.array(y)

X = X / 127.0
X = X.reshape((X.shape[0], X.shape[1], 1))
y = y / 127.0

# Build AI model
model = Sequential()
model.add(LSTM(128, input_shape=(sequence_length, 1)))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')

# Train model
model.fit(X, y, epochs=50, batch_size=2)

# Generate new music
pattern = X[0]
generated_notes = []

for i in range(30):
    prediction = model.predict(
        pattern.reshape(1, sequence_length, 1),
        verbose=0
    )

    predicted_note = int(prediction[0][0] * 127)
    predicted_note = max(0, min(127, predicted_note))

    generated_notes.append(predicted_note)

    pattern = np.append(
        pattern[1:],
        [[prediction[0][0]]],
        axis=0
    )

# Convert to MIDI
output_stream = stream.Stream()

for n in generated_notes:
    midi_note = note.Note(n)
    midi_note.quarterLength = 0.5
    output_stream.append(midi_note)

output_stream.write('midi', fp='generated_music.mid')

print("Music generated successfully!")
print("Output file: generated_music.mid")