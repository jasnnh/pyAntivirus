import os
import hashlib
import json
from collections import defaultdict
virusDB = defaultdict(list)

# Read JSON file
with open('virusDB.json', 'r') as file:
    virusDB = json.load(file)

def scan_file(d):

    if checkSignature(d):
        print("Malicious signature detected!")
        input('Do you want to delete? PRESS [ENTER]')
        os.remove(d)
        print("File deleted")
    else:
        print(f"File: '{d}' is clean.")

def checkSignature(file_path):
    try:
        print(file_path)
        with open(file_path, 'rb') as f:
            lines = f.readlines()
    
            count = 0
            # Strips the newline character
            for line in lines:
                count += 1
                file_content = hashlib.md5(line).hexdigest();
                print(file_content);
                for key, values in virusDB.items():
                    for i in values:
                        if i["hash"] in file_content:
                            return True;
        f.close(); 
        return False
    except FileNotFoundError:
        print("File not found.")
        return False

if __name__ == "__main__":

    scan_file("testVirus.txt")