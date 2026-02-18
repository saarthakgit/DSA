# numbers right angle triangle

class Solution :
    def number_right_triangle(N):
        for i in range(1,N+1):
            # print("new iter:",i)
            for j in range(i):
                print(int(j+1),end='')
            print()
sol = Solution

if __name__ == "__main__":
    sol.number_right_triangle(5)