# Number Crown Pattern

class Soln : 
    def crown(N):
        space = N*2-2
        for row in range(1,N+1):
            # no. of rows rows = N
            for col in range(1,N*2+1):
                # no. of col = 2N
                if(col<=N and col<=row):
                    print(col,end="")
            if(col>N):
                print(' '*(space),end="")
                space-=2
                for i in range(row,0,-1):
                    print(i,end="")
            print()

            




                
                

if __name__ == "__main__":
    Soln.crown(5)
    # Solution.crownNum(5)
