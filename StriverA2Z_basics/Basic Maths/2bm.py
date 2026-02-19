# reversal of number

class Sol:
    def reverse(N):
        # brute force approach
        if N == 0:
            return (1)
        n = N
        # remove trailing zeroes 
        while n%10 == 0:
            n = n//10
            # print(n)
        # if negative , add the minus sign
        if n<0:
            print("-", end="")
        # set the value to absolut
        n = abs(n)
        while n>0:

            print(n%10,end="")
            n = n//10
        print()

class Sol2 : 
    def reverse(N):
        revN = 0
        n=abs(N)
        # if n<0:
            
        while n>0:
            last_digit = n%10
            n=n//10
            revN = (revN*10)+last_digit
        if N<0:
            print(revN*-1)
        else:
            print(revN)




if __name__ == "__main__":
    # Sol.reverse(-778900)
    # print(Sol.reverse(0))
    # Sol.reverse(8080)
    Sol2.reverse(78090)
    Sol2.reverse(-78090)
    Sol2.reverse(0)