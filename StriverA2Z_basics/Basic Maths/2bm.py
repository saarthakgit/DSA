# reversal of number

class Sol:
    def reverse(N):
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
if __name__ == "__main__":
    Sol.reverse(-778900)
    print(Sol.reverse(0))
    Sol.reverse(8080)
        