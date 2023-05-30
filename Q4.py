# Q4
def celfar():
    list1 = [x for x in range(0,101,10)]
    for element in list1:
        result = element*9/5 + 32
    list2 = []
    list2 = list2.append(result)
    return list1,list2
print(celfar())