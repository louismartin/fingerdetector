import os.path as op
import os
import glob

recordings_dir = 'recordings'
if not op.exists(recordings_dir):
    os.makedirs(recordings_dir)

# Create new recording directory
dirs = glob.glob(op.join(recordings_dir, '[0-9]'*3)) # Match three digit dirs
if len(dirs) == 0:
    max_num = 0
else:
    max_num = max([int(dir_name.split('/')[-1]) for dir_name in dirs])
recording_dir = op.join(recordings_dir, '%03d' % (max_num + 1))
os.makedirs(recording_dir)

# TODO: start video thread and key recording thread
