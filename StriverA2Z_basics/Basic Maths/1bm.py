# Given an integer N, return the number of digits in N.
import math
class Solution:
    def numberofdigits(N):
        # brute force
        # print(len(str(N)))
        count = 0
        n = N
        while n>0:
            n = n//10 #floor division
            count+=1
        print(count)


class Sol2 : 
    # optimum:
    def numdig(N):
        count = math.log(N,10)
        print(int(count)+1)

if __name__=="__main__":
    Solution.numberofdigits(8989)
    Sol2.numdig(90)

