import types
import inspect

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

#myfilter is similar to filter function. It calls the given function and returns a list of favourable values from the input list.
def myfilter(func, inpAry):

    if type(inpAry) != list:
        print('Second Parameter shall be a List')
        return
    if type(func) != types.FunctionType:
        print('First Parameter shall be a function')
        return
    if len(inpAry) < 1:
        print('List shall contain atleast 1 element')
        return

    result = []
    for elem in inpAry:
		#call the input function with each element from the input list.
		#if the return value is true, add to the output list
        if func(elem) == True:
            result.append(elem)
    return result

#call the myfilter with a sample input and function.
res = myfilter(myFunc, ages)
print(res)
