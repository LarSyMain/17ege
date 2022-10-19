#------------------------------------------------------
# №1

f = open("17.txt")
a = [int(x) for x in f]

k = 0
m = 0

for i in range(len(a)-1):
	if a[i] % 3 == 0 or a[i+1] % 3 == 0:
		k += 1
		m = max(m, a[i] + a[i+1])
print(k, m)
#------------------------------------------------------
# №2

f = open("17(2).txt")
a = [int(x) for x in f]

k = 0
m = 0

for i in range(len(a)-1):
	if (a[i] + a[i+1]) % 3 == 0 and (a[i] + a[i+1]) % 6 != 0 and abs(a[i] * a[i+1]) % 10 == 8: # abs - берем число по модулю!
		k += 1
		m = max(m, a[i] + a[i+1])
print(k, m)
