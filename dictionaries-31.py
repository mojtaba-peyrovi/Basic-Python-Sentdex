exDict = {'Jack':15,'Bob':22,'Alice':12,'Kevin':17}
print(exDict['Jack'])
exDict['Tim'] = 14
print(exDict)
exDict['Tim'] = 15
print(exDict)
del exDict['Tim'] # DELTEES ONE ITEM
print(exDict)
exDictTwo = {'Jack':[15,'blode'],'Bob':[22,'black'],'Alice':[12,'brown'],'Kevin':[17,'red']}
print(exDictTwo['Jack'][1]) #references blonde
