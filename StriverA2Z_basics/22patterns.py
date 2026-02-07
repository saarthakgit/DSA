# Number Spiral

class sol:
    def spiral(N):
        n=N
        for render in range(1,N+1):
            for i in range(1,N*2):
                for j in range(1,N*2):
                    if(i==1 or i==N*2-1 or j==1 or j==N*2-1):
                        print(n,end="")
                    else:
                        print(" ",end="")
                
            print()


if __name__=="__main__":
    sol.spiral(4)