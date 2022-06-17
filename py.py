result = dict()

word = input ("masukkan input : ")

for i in word:
	if i == " " :
		continue
	I = i.lower()
	if not result.get(I):
		result [I] =0
	result [I] +=1
	
for i in result:
	print("%s : %d" % (i, result[i]))
