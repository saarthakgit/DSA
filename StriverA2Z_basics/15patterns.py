# Reverse Letter Triangle Pattern

class Sol:
    def rev_letter_triangle(N):
        for i in range(N,0,-1):
            for j in range(0,i):
                print(chr(65+j),end="")
            print()

if __name__=="__main__":
    Sol.rev_letter_triangle(5)
