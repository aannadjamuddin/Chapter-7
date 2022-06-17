file = open(input("masukkan nama file: "),"a")
add = True
while add:
    data = input("data yg ingin ditambahkan: ")
    file.write(data)
    add = input("mau lagi? (y/n): ") == 'y'
file.close()
    
