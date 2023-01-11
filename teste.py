l1 = [5,9,2]
l1.reverse()
list1=[str(i) for i in l1]
resList1 = "".join(list1)
print('Valor invertido de A: ' + resList1)

l2 = [1,6,4]
l2.reverse()
list2=[str(i) for i in l2]
resList2 = "".join(list2)
print('Valor invertido de B: ' + resList2)

resList = int(resList1)
resList2 = int(resList2)
result = resList + resList2
print('Soma de A e B: ' + str(result))

inverseResult = int(str(result)[::-1])
res = [int(x) for x in str(inverseResult)]
print('Resultado da soma ao inverso: ' + str(res))
