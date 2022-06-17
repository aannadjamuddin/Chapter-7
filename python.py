try:
    file = open('C:/data.txr','r')
    try:
        bil1 = int(file.readline())
        bil2 = int(file.readline())
        hasil = bil1 / bil2
        print(bil1, " dibagi ", bil2, " sama dengan ", hasil)
    except ZeroDivisionError:
        print('tidal boleh pembagian dengan nilai 0')
except FileNotFoundError:
    print('file tidak ditemukan')


