# repeater right triangle
class Solution : 
    def repeated_number_right_triangle(N) :
        for i in range(1,N+1):
            print(str(i)*i)
            

if __name__ == "__main__" : 
    sol  = Solution
    sol.repeated_number_right_triangle(5)