# Half diamond
# for n = 5, 
'''
*
**
***
****
*****
****
***
**
*
'''

class Soln : 
    # 2 loops
    def halfdiamond(N):
        for i in range(1,N+1):
            print('*'*i)
        for j in range(N-1,0,-1):
            print('*'*j)


class Soln2 :
    def halfdiamond(N):
        star = 1
        for i in range(1,N*2):
            print("*"*star)
            if i<N:
                star+=1
            elif i>=N:
                star-=1

if __name__ == "__main__":
    Soln.halfdiamond(5)
    print("\n")
    Soln2.halfdiamond(5)