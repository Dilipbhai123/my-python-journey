import os

try:
    os.rename("file/test_file.txt", "file/123.txt")
    print("file name change sacsessfull")
except FileNotFoundError:
    print("file is not found")