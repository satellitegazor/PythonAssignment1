
# program that returns a list as below 
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
xary = []
yary = []
zary = []

res2Ary = []
xval = yval = zval = ''
# inthe below loop, form an separate list for output formats of x, y and z
# join all the lists to one list.
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

# output #['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
print(resAry)
# output ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
print(res2Ary)

#res3Ary = [][]
mary = []

for m in range(0, 3):
    nary = []
    for n in range(2, 5):
        nary.append(n + m)
    mary.append(nary)
#output [[2, 3, 4], [3, 4, 5], [4, 5, 6]]
print(mary)

pary = []
for o in range(0, 4):
    oary = []
    for p in range(2, 6):
        oary.append(o + p)
    pary.append(oary)
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
print(pary)


oary = []
for k in range(1, 4):
    for l in range (1, 4):
        inary = []
        inary.append(k)
        inary.append(l)
        oary.append(inary)
# [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
print(oary)
