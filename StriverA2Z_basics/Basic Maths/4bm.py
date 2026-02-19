# gcd
class Sol:
    def gcd(N1,N2):
        rootcheckof = 0
        gcd = 1
        if N1>N2:
            rootcheckof = N2
        else:
            rootcheckof = N1
        for i in range(2,int(rootcheckof)+1):
            if N1%i ==0 and N2%i == 0:
                gcd = i
        print(gcd)
        

if __name__ == "__main__":
    Sol.gcd(20,18)