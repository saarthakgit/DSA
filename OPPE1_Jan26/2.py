# Write a function divide_into_almost_equal_parts(n: int, k: int) -> list that takes two integers, n and k, and creates a list of size k where the elements are approximately equal and sum up to n. The list should contain larger numbers towards the beginning.

def divide_into_almost_equal_parts(n: int, k: int):
    lst = []
    if n%k==0:
        for i in range(0,k):
            lst.append(int(n/k))
    elif n%k!=0:
        # eg. (5,3)
        least = n//k
        maxm = least+1
        
        leasttimes = 0
        maxtimes = k-leasttimes

        for i in range(0,k):
            if least*leasttimes+maxtimes*maxm!=n:
                leasttimes+=1
                maxtimes=k-leasttimes
            else:
                break
        # print(maxtimes,leasttimes)
        lst = [maxm]*maxtimes + [least]*leasttimes
    return lst 


print(divide_into_almost_equal_parts(5, 3))
print(divide_into_almost_equal_parts(16, 3))
print(divide_into_almost_equal_parts(12, 4))
print(divide_into_almost_equal_parts(10, 3))