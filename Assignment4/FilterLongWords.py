def filter_long_words(strList, length):

    resList = []
    for s in strList:
        if len(s) > length:
           resList.append(s)
    return resList;


stringlist = {'Bangalore', 'Hyderabad', 'Mumbai', 'Pune', 'Patna'}
resultList = filter_long_words(stringlist, 6)
print(resultList)
