import os 
from pathlib import Path
def get_filepath():
    user=input("Enter the path to the file: ")
    file_path = Path(user)
    if not file_path.exists():
        print("The specified file does not exist.")
        return None
    else:
        return file_path


