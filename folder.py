# script to create folders for collections

import os
import numpy as np

# path for exported data, numpy arrays
DATA_PATH = os.path.join('MP_DATA')

# actions that we try to detect
# sequence of data is used for detection, not single frame
actions = np.array(['hello', 'thanks', 'iloveyou'])

# 30 videos worth of data
no_sequences = 30

# each video is 30 frames in length
sequence_length = 30


# for each action make a folder, and a folder for each sequence of action
for action in actions:
        for sequence in range(no_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
            except:
                pass