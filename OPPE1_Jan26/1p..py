# what came what times
n = int(input())
its=[]
for i in range(0,n):
    nums = input()
    its.append(nums)

result = []
for i in its:
    # 443322
    index = 1
    count = 1
    # print("running i",i)
    for j in i:
        # print("runnning j",j ,"withindex:",index)
        if index!=len(i) and j == i[index] :
            count+=1
            # print("count updated")
        else:
            result += [str(j)]+[str(count)]
            count = 1
            # print("next element was unique, appended")
        index+=1
    result.append("\n")
print( "".join(result))