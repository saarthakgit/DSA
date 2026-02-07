# Symmetric-Void Pattern

class soln :
    def symmetric_void(N) :
        space_before_mid = 0
        space_after_mid = N*2-2
        for j in range(N,0,-1):
            print("*"*j+" "*space_before_mid+"*"*j)
            space_before_mid+=2
        for i in range(1,N+1):
            print("*"*i+" "*space_after_mid+"*"*i)
            space_after_mid-=2

if __name__ == "__main__":
    soln.symmetric_void(5)
