entry = dict()

#fungsi untuk menambah entry
def addEntry(name, price):
    global entry

    #cek jika entri sudah ada jika ada return false
    if entry.get(name):
        print("entri sudah ada")
        return False
    entry[name] = price
    return True

while True:
    addEntry(input("masukkan nama buah : "), int(input("masukkan harga : ")))
    #cek input user jika ingin lanjut input entry
    if input("input lagi? y/n : ") == "n":
        break

#print setiap entri yang ada
for i in entry:
    print("%s : Rp %d" % (i, entry[i]))
