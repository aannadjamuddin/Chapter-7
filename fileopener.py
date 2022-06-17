path = input('masukkan nama file: ')
try:
    file = open(path, "r")
    print("is file %s adalah:" % (path))
    print(file.read())
except FileNotFoundError:
    print("file tidak ditemukan")
