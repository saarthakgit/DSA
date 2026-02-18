# Increasing Letter Triangle Pattern

class Solution : 
    def inc_letter_triangle(N):
        for i in range(0,N):
            for j in range(0,i+1):
                print(chr(65+j),end="")
            print()

if __name__=="__main__":
    Solution.inc_letter_triangle(5)