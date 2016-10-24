import cv2
import os
import os.path as op
import glob

class Saver:
    def __init__(self):
        self.recordings_dir = 'recordings'
        if not op.exists(self.recordings_dir):
            os.makedirs(self.recordings_dir)
        self.clean()
        dir_num = self.get_dir_num(self.recordings_dir)

        # Create new recording directory
        self.recording_dir = op.join(self.recordings_dir, '%03d' % dir_num)
        os.makedirs(self.recording_dir)

    def get_dir_num(self, root):
        # Match three digit directories
        dirs = glob.glob(op.join(root, '[0-9]'*3))

        if len(dirs) == 0:
            dir_num = 1
        else:
            max_num = max([int(dir_name.split('/')[-1]) for dir_name in dirs])
            dir_num = max_num + 1
        return dir_num

    def clean(self):
        # Remove empty directories
        dirs = glob.glob(op.join(self.recordings_dir, '[0-9]'*3))
        for dir_name in dirs:
            try:
                os.rmdir(dir_name)
            except OSError as ex:
                pass #print('dir not empty')

    def save_frames(self, finger, frames):
        finger_dir = op.join(self.recording_dir, 'finger_%s' % finger)
        dir_num = self.get_dir_num(finger_dir)
        save_dir = op.join(finger_dir, '%03d' % dir_num)
        os.makedirs(save_dir)
        for i, frame in enumerate(frames):
            filename = op.join(save_dir, 'frame_%03d.jpg' % i+1)
            cv2.imwrite(filename, frame)
