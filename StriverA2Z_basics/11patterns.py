# binary triangle

class Solution:
    def binarytriangle(N):
        # N is no. of rows
        for i in range(1,N+1):
            # print("agn")
            if(i%2==0):
                # print("0")
                for j in range(1,i+1):
                    # print("1",end="")
                    if(j%2!=0):
                        print("0",end="")
                    elif(j%2==0):
                        print("1",end="")
                # print()
            elif (i%2!=0):
                # print("1")
                for j in range(1,i+1):
                #  print("0",end="")
                    if(j%2!=0):
                        print("1",end="")
                    elif(j%2==0):
                        print("0",end="")
            print()
            

if __name__=="__main__":
    Solution.binarytriangle(5)
    
# sol2 : use matrices