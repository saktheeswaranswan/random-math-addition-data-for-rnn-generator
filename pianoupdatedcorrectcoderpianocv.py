import cv2
import pandas as pd

# Load the key mapping from notes to positions on the mini keyboard
key_mapping = {
    
    'C#': (332, 329),
    'D': (399, 242),
    'D#': (399, 242),
    'E': (371, 231),
    'E#': (140, 280),
    'F': (349, 239),
    'F#': (409, 324),
    'G': (245, 265),
    'G#': (280, 260),
    'A': (296,236),
    'A#': (350, 250),
    'B': (270,233),
    'C': (426,241),
    
}

# Load the entries from the csv file
entries = pd.read_csv('/home/saktheeswaran/piano for all/notespia.csv')

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('keyboard_with_mark.mp4', fourcc, 20.0, (720, 640))
cv2.namedWindow("keyboard_with_mark", cv2.WINDOW_NORMAL)
cv2.resizeWindow("keyboard_with_mark", 640, 480)


# Open a window to display the video feed
cv2.namedWindow("keyboard_with_mark", cv2.WINDOW_NORMAL)

# Start the webcam stream
cap = cv2.VideoCapture(0)

# Loop through each entry in the csv file
for index, row in entries.iterrows():
    note = row['Note']
    center_x, center_y = key_mapping[note]
    duration = row['Duration']
    
    # Read a frame from the webcam stream
    ret, frame = cap.read()
    
    # Draw a red circle at the center of the key on the mini keyboard image
    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
    
    # Write the frame to the video file
    out.write(frame)
    
    # Display the video feed
    cv2.imshow("keyboard_with_mark", frame)
    
    # Wait for the specified duration before displaying the next entry
    cv2.waitKey(duration)

# Release the video writer and close the window
out.release()
cv2.destroyAllWindows()

