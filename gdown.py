#!/usr/bin/env python3

import requests
from zipfile import ZipFile
import argparse

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('id', default=None, type=str, help='file id.')
    parser.add_argument('filename', default=None, type=str, help='file name')
    parser.add_argument('--zip', action='store_true', help='unzip file')
    args, _ = parser.parse_known_args()
    
    
    file_id = args.id
    destination = f'Downloads/{args.filename}' if args.zip else f'weights/{args.filename}'
    print(f'Start download {args.filename} to {destination}')
    download_file_from_google_drive(file_id, destination)
    
    if args.zip:
        print(f'Start Unzip {args.filename}')
        zip = ZipFile(destination)
        zip.extractall('./weights')
        
    print("Finished")