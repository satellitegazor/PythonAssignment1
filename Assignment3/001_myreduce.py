import types
import inspect
from functools import reduce

# Returns the sum of two elements
def sumTwo(a,b,c):
    return a+b+c


def myreduce(func, inpAry):
    
    if type(inpAry) != list:
        print('Second Parameter shall be a List')
        return
    if type(func) != types.FunctionType:
        print('First Parameter shall be a function')
        return
    if len(inpAry) < 2:
        print('List shall contain atleast 2 elements')
        return
    
    ispt = inspect.getfullargspec(func)
    print(ispt)

    arglen = len(ispt.args)
    print('Arg Len: ' + str(arglen))
    
    inputLen = len(inpAry)
    inpCtr = 0
    ## retval = inpAry[0]

    while inpCtr < (inputLen - 1):
        
        paramCtr = 1
        paramAry = []        

        if inpCtr == 0:
            retval = inpAry[0]

        paramAry.append(retval)
        while paramCtr < arglen:
            #print(inpCtr + paramCtr)
            paramAry.append(inpAry[inpCtr + paramCtr])
            paramCtr += 1
            
        #print(paramAry)
        retval = func(*paramAry)
        #print(retval)
        
        inpCtr += (arglen - 1)
        #print(inpCtr)
        
    return retval

Ary = [2, 3, 4, 5, 6, 8 , 9, 10, 11]
g = myreduce(sumTwo, Ary)
print(g)