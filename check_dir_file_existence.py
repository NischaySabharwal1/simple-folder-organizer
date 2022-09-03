import os
import time 

d = time.strftime("%d-%m-%Y")
t = time.strftime("%H-%M-%S")

def rename_file(s):
    if os.path.exists(s):
        str, dst = "","\\"
        loc = s.split('\\')[:-1]
        fname = s.split('\\')[-1]
        lst = fname.split('.')
        str = str.join(lst[:-1])+f'_{d}_{t}.'+lst[-1]
        dst = dst.join(loc)+f'\\{str}'
        return dst
    else:
        return s

def check_dir(s):
    if not os.path.exists(s):
        os.makedirs(s, exist_ok=True)