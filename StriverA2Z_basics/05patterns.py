# inverted right triangle

class Solution :
    def inverted_triangle(N) :
        n = N
        while n>0:
            print('*'*n)
            n-=1


if __name__ == "__main__":
    sol = Solution
    sol.inverted_triangle(5)
    