# actly consecutive loongest chain here
n = int(input())
words = []
for i in range(0,n):
    word = input()
    words.append(word)

maxcount = 0
index = 1
count = 1
for j in words:
    if index<len(words):
        nextword = words[index]
        if j[-1]==nextword[0]:
            count+=1
            if count>maxcount:
                maxcount = count
        else:
            count = 1
        index+=1

print(maxcount)