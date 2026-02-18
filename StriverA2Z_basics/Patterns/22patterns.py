# Number Spiral

class sol:
    def spiral(N):
        for i in range(1,N*2):
            top = i-1
            bottom = (N*2-1)-i
            for j in range(1,N*2):
                left = j-1
                right = (N*2-1)-j
                Value = min(top,bottom,left,right)
                # if()
                print(N-Value,end="")
                
            print()


if __name__=="__main__":
    sol.spiral(4)