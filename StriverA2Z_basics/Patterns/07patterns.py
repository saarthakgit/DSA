# pyramid

class Solution : 
    def pyramid(rows):
        space = rows - 1
        for stars in range(1,rows*2,2):
              print(' '*space + '*'*stars)
              space-=1
                   
              
            
    
if __name__ == '__main__':
    sol = Solution
    sol.pyramid(5)