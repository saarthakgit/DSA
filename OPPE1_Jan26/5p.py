# replace middle with n times
n=int(input())
tu = tuple(input())
if len(tu)%2!=0:
    # (0,1,2)
    midindex = int((len(tu)-1)/2)
    first = tu[0:midindex]
    last = tu[midindex+1:]
    print(first+tuple(tu[midindex])*n+last)