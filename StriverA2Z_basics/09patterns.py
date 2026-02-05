# diamond pattern
# n*2 times rows, middle 2 being the longest and equal
# odd no. of stars only

class Solution1 : 
    # using 2 loops

    def diamond(N):
        space_decreasing = N-1
        space_increasing = 0
        for i in range(1,N*2,2):
            print(" "*space_decreasing + '*'*i)
            space_decreasing -=1
        for j in range(N*2-1,0,-2):
            print(" "*space_increasing+"*"*j)
            space_increasing+=1


if __name__ == "__main__":
    sol1 = Solution1
    sol1.diamond(5)