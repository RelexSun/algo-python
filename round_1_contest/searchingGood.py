a = input()
t = input()
j, count = 0, 0
newLst = []
for i in range(len(a), len(t)+1, len(a)):
    if a == t[j:i]:
        count += 1
        newLst.append(i+1-len(a))
    j = i
print(count)
for i in newLst:
    print(i, end=" ")


