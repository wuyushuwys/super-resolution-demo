from pathlib import Path
import shutil
import os
from glob import glob
import logging
import sys


def folder_init(parent, folder):
    dirpath = Path(parent, folder)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)
    os.mkdir(f'{parent}/{folder}')
    

def folder_create(parent, folder):
    dirpath = Path(parent, folder)
    if dirpath.exists() and dirpath.is_dir():
        pass
    else:
        os.makedirs(f'{parent}/{folder}')
        
def folder_remove(parent, folder):
    dirpath = Path(parent, folder)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)
        

def get_weight_name(args):
    files = glob('weights/*')
    for f in files:
        if str(args.scale) in f and args.model_size in f:
            return f
    logging.error('No such weights. Please select a new one.')
    sys.exit()
    

def get_inputs_name():
    files = glob('inputs/*')
    return [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')) ]
    
    
    