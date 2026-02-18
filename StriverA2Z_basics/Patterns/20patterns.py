#  butterfly

class sol :
    def butterfly(N):
        space_till_mid = N*2-2
        space_after_mid = 2
        for i in range(1,N+1):
            print("*"*i+" "*space_till_mid+"*"*i)
            space_till_mid-=2
        for j in range(N-1,0,-1):
            print("*"*j+" "*space_after_mid+"*"*j)
            space_after_mid += 2 

if __name__ == "__main__":
    sol.butterfly(5)