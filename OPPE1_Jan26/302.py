ifn = input()
order  = ifn.split(" ")


index = 1
for i in range(1,4):
    for j in range(1,4):
        if i==2:
            position = (i+j)+1
        elif i==3:
            position = (i+j)+3
        else:
            position = i*j
        if str(position) in order:
            print(index,end="")
            index+=1
        else:
            print("[]",end="")
    print()

# order = [1 3 6 9] 
# 1 [] 2