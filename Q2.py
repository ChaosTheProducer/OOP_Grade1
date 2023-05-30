# Q2
def countzodiac(year):
    list1 = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare', 'Dragon', 'Snake', 'Horse', 'Sheep']
    return(f'{year} is the year of {list1[int(year)%12]}')
print(countzodiac(2011))