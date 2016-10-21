import time
import pandas as pd
from getcharacter import _Getch

class Detector:
    def __init__(self):
        self.finger_keys = {
            '1': ['1','q','a','z'],
            '2': ['2','w','s','x'],
            '3': ['3','e','d','c'],
            '4': ['4','r','f','v','5','t','g','b'],
            '7': ['6','y','h','n','7','u','j','m'],
            '8': ['8','i','k',','],
            '9': ['9','o','l','.'],
            '10': ['0','p',';','/','-','[','\'','=',']','\\']
        }

    def run(self):
        self.start_time = time.time()
        getch = _Getch()
        for i in range(10):
            key = getch()
            hit_time = time.time() - self.start_time
            finger = self.get_finger(key)
            print('%s hit with finger %s at %f' % (key, finger, hit_time))
            
    def get_finger(self, key):
        for finger, keys in self.finger_keys.items():
            if key in keys:
                return finger
        return None
                      
