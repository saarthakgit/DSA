oo = input()
newoo = oo[::-1]
result =""
index = 0
for i in oo:
    if i.lower() in "aeiou":
        i = newoo[index-1]
    result+=i 
    index +=1

print(result)
