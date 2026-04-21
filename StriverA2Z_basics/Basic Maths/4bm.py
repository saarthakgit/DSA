# gcd
class Sol:
    # def gcd(N1,N2): 
    #     # check goin upwards
    #     rootcheckof = min(N1,N2)
    #     gcd = 1
        
    #     for i in range(2,int(rootcheckof)+1):
    #         if N1%i ==0 and N2%i == 0:
    #             gcd = i
    #     print(gcd)
    # def gcd(N1,N2): 
    #     # check goin downwrds
    #     checkfrom = min(N1,N2)
    #     gcd = 1
        
    #     for i in range(checkfrom,1,-1):
    #         if N1%i ==0 and N2%i == 0:
    #             gcd = i
    #             break
    #     print(gcd)
    #  def gcd(N1,N2): 
    #     # euclidean algo => 
    #     b = min(N1,N2)
    #     a = max(N1,N2)
    #     c = min(a-b,b)
    #     gcd = 1
    #     # hcf(a,b) = hcf(a-b,b) , where a > b

    #     for i in range(c,1,-1):
    #         if N1%i ==0 and N2%i == 0:
    #             gcd = i
    #             break
    #     print(gcd)
      
        
        # def gcd(N1,N2):
        #       a = max(N1,N2)
        #       b = min(N1,N2)
        #       gcd = 1
        #       while a>0 and b>0:
        #             b = a%b
                    


        

if __name__ == "__main__":
    Sol.gcd(20,18)