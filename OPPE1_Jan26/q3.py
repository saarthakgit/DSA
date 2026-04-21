n = int(input())
rows = []
for i in n(0,n):
    row = input()
    rows.append(row.split(","))

row = 1
col = 1
diagonal = []
lowtriangle = []
uptriangle = []
for i in rows:
    for j in i:
        if row==col:
            diagonal.append(j)
        elif row>col and j!=0:
            print("NOT DIAGONAL")
            break
        elif row<col and j!=0:
            print("NOT DIAGNL")
            break
    row+=1
    col+=1 

for j in diagonal:
    if max(diagonal) == min(diagonal):
        if max(diagonal)==1:
            print("IDENTITY")
        else:
            print("SCALAR")
if max(lowtriangle) ==0 and max(uptriangle)==0:
    print("DIAGONAL")

