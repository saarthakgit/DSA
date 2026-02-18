# Increasing Number Triangle Pattern

class Sol:
    def inc_number_triangle(N):
        const = 1
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(const,end=" ")
                const+=1
            print()
    
if __name__ == "__main__":
    Sol.inc_number_triangle(5)