lagi = True
total = 0
jumlah = 0
while lagi:
    try:
        n = int(input("masukkan bilangan bulat: "))
        total = total + n
        jumlah = jumlah + 1
        lagi = input("lagi? (y/n): ") == 'y'
    except ValueError:
        print("bukan bilangan bulat")

print("rata-ratanya adalah %d" % (total / jumlah))
