# Определить, какое число в массиве встречается чаще всего.

qww =[1,3,3,4,5 ,5]
ddd={}
for i in range(len(qww)):
    ddd[qww[i]]=qww.count(qww[i])
print (ddd)
asd = max(ddd.values())
print(asd)
zxc = 0
for k,v in ddd.items():
    if ddd[k] == asd:
        zxc = k
        break
print (zxc)


