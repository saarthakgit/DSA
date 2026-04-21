n = input()
n = n.split(",")
cleanN = []
for i in n:
    cleanN.append(int(i.strip()))
# [0,1,2,3]
halfindex = int(len(cleanN)/2)
lefthalf =  cleanN[0:halfindex]
righthalf = cleanN[halfindex:]
# print(sum(lefthalf))
if sum(lefthalf)>sum(righthalf):
    print("LEFT HEAVY")
elif sum(lefthalf)<sum(righthalf):
    print("RIGHT HEAVY")
else:
    print("BALANCED")