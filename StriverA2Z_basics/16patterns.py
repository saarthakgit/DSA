# Alpha-Ramp Pattern

class Soln :
    def ramp_pattern(N):
        for i in range(1,N+1):
            j = i-1
            print(chr(65+j)*i,end="")
            print()

if __name__ == "__main__":
    Soln.ramp_pattern(5)