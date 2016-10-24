from collections import deque
import cv2
from detector import Detector
from saver import Saver

sv = Saver()

det = Detector()
cap = cv2.VideoCapture(1)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

n_frames = 5 # Number of frames to store
frames = deque(range(n_frames)) # Store rolling frames
delayed = deque([])
n_keys_hit = 0
i_frame = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        i_frame += 1
        frames.append(frame)
        frames.popleft()
        out.write(frame)

        cv2.imshow('frame', frame)
        unicode_key = cv2.waitKey(1) & 0xFF
        if unicode_key != 255:
            if unicode_key == 27: # Press escape to end program
                break
            n_keys_hit += 1
            key = chr(unicode_key)
            finger = det.get_finger(key)
            print(key)

            # Delay the saving of frames
            save_frame = i_frame + int(2/3*n_frames)
            delayed.append((save_frame, finger))

        # Save frames
        if len(delayed) != 0 and i_frame == delayed[0][0]:
            finger = delayed[0][1]
            sv.save_frames(finger, frames)
            delayed.popleft()
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
