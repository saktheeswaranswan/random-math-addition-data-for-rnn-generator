# -*- coding: utf-8 -*-
"""midi-extractor-csv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lwrf7C3xPvA48i-Yo7IQK0qd10KzhxrS
"""

!pip install mido

import mido
import csv

# Set the file name and track number to extract notes from
file_name = '/content/xdffdgf.mid'
track_num = 0

# Open the MIDI file and select the desired track
midi_file = mido.MidiFile(file_name)
track = midi_file.tracks[track_num]

# Define a list to hold the extracted notes and their durations
notes = []

# Iterate through each MIDI message in the track
for msg in track:
    # Check if the message is a Note On event with a nonzero velocity (i.e. the note is being played)
    if msg.type == 'note_on' and msg.velocity != 0:
        # Append a tuple containing the note value and its duration (in ticks) to the notes list
        notes.append((msg.note, msg.time))

# Find the tempo message that sets the tempo of the MIDI file
tempo = None
for msg in midi_file:
    if msg.type == 'set_tempo':
        tempo = msg.tempo
        break

# Convert the tick values to seconds based on the tempo (in microseconds per quarter note) of the MIDI file
if tempo is not None:
    tempo = mido.tempo2bpm(tempo)
    tempo = 60 / tempo
    notes = [(note, duration * tempo) for note, duration in notes]
    #notes = [(note, duration * tempo * 1000) for note, duration in notes]

# Write the notes list to a CSV file
with open('notes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Note', 'Duration'])
    for note, duration in notes:
        writer.writerow([note, duration])

#rest without tempo

import mido
import csv

# Set the file name and track number to extract notes from
file_name = 'example.mid'
track_num = 0

# Open the MIDI file and select the desired track
midi_file = mido.MidiFile(file_name)
track = midi_file.tracks[track_num]

# Define a list to hold the extracted notes and their durations
notes = []

# Iterate through each MIDI message in the track
for msg in track:
    # Check if the message is a Note On event with a nonzero velocity (i.e. the note is being played)
    if msg.type == 'note_on' and msg.velocity != 0:
        # Append a tuple containing the note value and its duration (in ticks) to the notes list
        notes.append((msg.note, msg.time))

# Convert the tick values to seconds based on the tempo (in microseconds per quarter note) of the MIDI file
tempo = midi_file.tracks[0][0].tempo
tempo = mido.tempo2bpm(tempo)
tempo = 60 / tempo
notes = [(note, duration * tempo) for note, duration in notes]

# Write the notes list to a CSV file
with open('notes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Note', 'Duration'])
    for note, duration in notes:
        writer.writerow([note, duration])

import mido
import csv

# Set the file name and track number to extract notes from
file_name = 'example.mid'
track_num = 0

# Open the MIDI file and select the desired track
midi_file = mido.MidiFile(file_name)
track = midi_file.tracks[track_num]

# Define a list to hold the extracted notes and their durations
notes = []

# Iterate through each MIDI message in the track
for msg in track:
    # Check if the message is a Note On event with a nonzero velocity (i.e. the note is being played)
    if msg.type == 'note_on' and msg.velocity != 0:
        # Append a tuple containing the note value and its duration (in ticks) to the notes list
        notes.append((msg.note, msg.time))

# Convert the tick values to seconds based on the tempo (in microseconds per quarter note) of the MIDI file
tempo = midi_file.ticks_per_beat * 500000 / midi_file.tempo
notes = [(note, duration * tempo) for note, duration in notes]

# Write the notes list to a CSV file
with open('notes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Note', 'Duration'])
    for note, duration in notes:
        writer.writerow([note, duration])