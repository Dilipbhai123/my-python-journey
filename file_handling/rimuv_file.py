import os

if os.path.exists("file/123.txt"):
    os.remove("file/123.txt")
    print("file deleyed sucsessfull")
else:
    print("file not found")