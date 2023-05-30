# Q3
def ifleapyear(yearnum):
    yearnum = int(yearnum)
    if yearnum % 400 ==0:
        return 'It is a leap year'
    elif yearnum % 100 == 0 :
        return 'It is not a leap year'
    elif yearnum % 4 == 0 :
        return 'It is a leap year'
    else :
        return 'It is not a leap year'
print(ifleapyear(2000))
print(ifleapyear(2005))
print(ifleapyear(2013))
print(ifleapyear(2020))
