# inverted pyramid

class Solution :
    def inverted_pyramid(N):
        # N = 5 means 5 rows , biggest row = 9 stars , smallest = 1 star
        space = 0
        for j in range(N*2-1,0,-2):
            print(" "*space + '*'*j)
            space +=1
        

if __name__ == '__main__':
    sol = Solution
    sol.inverted_pyramid(3)
