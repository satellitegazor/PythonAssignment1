import types
import inspect
from functools import reduce

# Returns the sum of three elements
def sumTwo(a,b,c):
    return a+b+c

#myreduce is similar to reduce. It accepts two parameters 1. FunctionName and InputValues Array
#myreduce will call the input function with the given input values iteratively and returns a single result value
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

	# arglen is the count of parameters in the input function to be called
    arglen = len(ispt.args)

    
	#inputLen is the count of values in the input list
    inputLen = len(inpAry)
    inpCtr = 0
    ## retval = inpAry[0]

	#In the below while loop, construct an array of input values sufficient to call the given function.
	#If the input values are more than the function arguments, then the result of previous output will be first input param in the subsequent iteration.
    while inpCtr < (inputLen - 1):
        
        paramCtr = 1
        paramAry = []        

        if inpCtr == 0:
            retval = inpAry[0]

		## Construct parameter Array
		## The first parameter value shall be the result of previous call to the input function
        paramAry.append(retval)
        while paramCtr < arglen:
            #print(inpCtr + paramCtr)
            paramAry.append(inpAry[inpCtr + paramCtr])
            paramCtr += 1
            
        #call the input function and record the result to be used as input in the next iteration
        retval = func(*paramAry)
        #print(retval)
        
		#move on to the next set of input values for the next iteration
        inpCtr += (arglen - 1)
        #print(inpCtr)
        
    return retval

#call the myreduce with a sample input values.
Ary = [2, 3, 4, 5, 6, 8 , 9, 10, 11]
g = myreduce(sumTwo, Ary)
print(g)