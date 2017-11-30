list = []
rainfall = input("Enter monthly rainfall separated by a space eg. 22 33 44(mm per day): ")
list = rainfall.split(" ")

highestFall = max(list)
print("The highest recorded rainfall is:",highestFall)

lowestFall = min(list)
print("The lowest recorded rainfall is:",lowestFall)

total = 0
for x in rainfall:
    total += float(x)
for i in range(len(rainfall)):
    len = float(rainfall[i])

averageFall = total/len
print("The average rainfall is equivalent to:",averageFall)

totalFall = print(list)
total = 0
for i in list:
    total += float(i)
print("The total is equivlent to:",total)