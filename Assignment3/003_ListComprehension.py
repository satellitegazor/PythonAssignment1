xary = []
yary = []
zary = []

res2Ary = []
xval = yval = zval = ''
for i in range(0, 4):
    xval += 'x'
    xary.append(xval)
    
    yval += 'y'
    yary.append(yval)
    
    zval += 'z'
    zary.append(zval)
    
    res2Ary.append(xval)
    res2Ary.append(yval)
    res2Ary.append(zval)

resAry = [];
resAry.append(xary)
resAry.append(yary)
resAry.append(zary)
print(resAry)
print(res2Ary)

#res3Ary = [][]
mary = []

for m in range(0, 3):
    nary = []
    for n in range(2, 5):
        nary.append(n + m)
    mary.append(nary)
print(mary)

pary = []
for o in range(0, 4):
    oary = []
    for p in range(2, 6):
        oary.append(o + p)
    pary.append(oary)
print(pary)


oary = []
for k in range(1, 4):
    for l in range (1, 4):
        inary = []
        inary.append(k)
        inary.append(l)
        oary.append(inary)
print(oary)
