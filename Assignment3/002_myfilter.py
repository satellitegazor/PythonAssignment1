import types
import inspect

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

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
        if func(elem) == True:
            result.append(elem)
    return result

res = myfilter(myFunc, ages)
print(res)
