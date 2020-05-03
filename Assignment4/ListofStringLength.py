def MapListOfWords(StringList):

    if type(StringList) != list:
        print('Input parameter must be a list')
        return

    resultList = []
    for s in StringList:
        resultList.append(len(s))

    return resultList

stringlist = ['Bangalore', 'Hyderabad', 'Mumbai', 'Pune', 'Patna']
print(type(stringlist))
LengthList = MapListOfWords(stringlist)
print(LengthList)
