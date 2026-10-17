data = ["this is test line.\n", "this is writelines add.\n", "I AM python Devaloper.\n", "machin language for python c++ java mysql rubi dot......\n"]

with open("file/file_handaling_with_function.txt", "w") as file:
    contant = file.writelines(data)
    print("file create and deta add sucsessfull")