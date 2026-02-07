# boundary

class sol:
    def boundary(N):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if(i==1 or j==1 or i==N or j==N):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
if __name__ == "__main__":
    sol.boundary(5)