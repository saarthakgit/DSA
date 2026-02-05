# 5*5 pattern using loops

# soln : 
class Solution :
    def rectangular_pattern(N):
        for i in range(N):
            for j in range(N):
                print('*',end='')
             #correct newline approach after printing horizontally   
            print()

    
sol = Solution
sol.rectangular_pattern(5)


# pseudocode - if using nested loops: 
''' for i in 1 to 5 inclusive,
 print newline
 run a loop for same range on every iteration == that prints without a new line
'''

# else without loops - 
'''
for i in range 5, print (*****)
'''

# my attempt
# for i in range(5):
#     print('\n')
#     for j in range(5):
#         print('*',end="")
    