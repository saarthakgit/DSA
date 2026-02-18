# Alpha-Hill Pattern

class Soln :
    def alpha_pattern(N):
        space=N-1
        for i in range(1,N+1):
            print(" "*space,end="")
            k = 0
            l = i-1
            # l = req no. of elements in last sequence
            for j in range(1,N*2):
                if(j<=i):
                    print(chr(65+k),end="")
                    k+=1
                if(j>i and l>0 and l<=i-1):
                    print(chr(64+l),end="")
                    l-=1

                
                
            print()
            space-=1

if __name__ =="__main__":
    Soln.alpha_pattern(4)
