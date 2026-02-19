# check if palindrome number
import math 

class Solution:
    # def checkpalindrome(N):
        # if N<0:
        #     return False
        # n = abs(N)
        # revN = 0
        # numberofdigits = int(math.log(n,10)+1)
        # # print(numberofdigits)
        # while n>0:
        #     lastdigit = n%10
        #     revN = revN*10 + lastdigit
        #     # odd 
        #     if numberofdigits % 2!=0:
        #         if revN == n:
        #             return True
        #         else:
        #             n=n//10
        #             # continue
        #     # even
        #     elif numberofdigits % 2 == 0 :
        #         n=n//10
        #         if revN == n:
        #             return True
                
        #     else :
        #         return False

        def checkpalindrome(N):
            if N<0 or (N!=0 and N%10==0):
                return False
            
            n=N
            revN=0
            while n>revN:
                lastdigit = n%10
                revN = revN*10+ lastdigit
                n=n//10
            # return revN,n 
            if revN//10==n or revN==n:
                     return True
            else:
                  return False
                

if __name__ == "__main__":
    print(Solution.checkpalindrome(5995))
    print(Solution.checkpalindrome(121))
    print(Solution.checkpalindrome(10))
