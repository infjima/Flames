nameOfBoy = list(input("Enter boy's name : ").lower())
nameOfGirl = list(input("Enter Girl's name : ").lower())
number = 0
flames = ['f', 'l', 'a', 'm', 'e', 's']
if ' ' in nameOfBoy:
    while ' ' in nameOfBoy:
        nameOfBoy.remove(' ')
if ' ' in nameOfGirl:
    while ' ' in nameOfGirl:
        nameOfGirl.remove(' ')

if len(nameOfBoy) > len(nameOfGirl):
    longerName = nameOfBoy
    smallerName = nameOfGirl
else:
    longerName = nameOfGirl
    smallerName = nameOfBoy
lengthOne = max(len(nameOfBoy), len(nameOfGirl))
lengthTwo = min(len(nameOfBoy), len(nameOfGirl))
nameOfBoy2 = []
for i in range(0, lengthOne):
    if longerName[i] in smallerName:
        smallerName.remove(longerName[i])
    else:
        nameOfBoy2.append(longerName[i])
# print(smallerName)
# print(nameOfBoy2)
totallength = len(smallerName)+len(nameOfBoy2)
# print(totallength)
value = 0
for i in range(6, 1, -1):
    value = ((value+totallength) % i)
    if value == 0:
        flames[i-1]
        flames.pop(i-1)
    else:
        flames.pop((value-1))
        value -= 1
print(flames)
