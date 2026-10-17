file = open("file/First_file.txt", "r")

data = file.readlines()

file.close()
print(data)