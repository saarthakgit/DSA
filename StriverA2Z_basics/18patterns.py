# Alpha-Triangle Pattern

class Sol:
    def alpha_triangle(N):
        # n = N+1
        for i in range(1,N+1):
            k  =   N-i+1
            for j in range(1,i+1):
                print(chr(64+k),end="")
                k+=1
            print()



if __name__ == "__main__":
    Sol.alpha_triangle(5)
