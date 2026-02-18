# inverted pattern with numbers

class Solution : 
    def inverted_number_triangle(N):
        for i in range (N,0,-1):
            for j in range (1,i+1):
                print(j,end='')
            print()

if __name__ == "__main__":
    sol = Solution
    sol.inverted_number_triangle(5)