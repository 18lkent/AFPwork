words = []
sentence = input("Enter a sentence: ")
words = sentence.split(' ')
print(words)

points = []
gamePoints = input("Enter the points for each game played eg. 5,6,7,8 ")
points = gamePoints.split(",")
print(points)

total = 0
for c in points:
    total += int(c)
    print(total)
print(total)