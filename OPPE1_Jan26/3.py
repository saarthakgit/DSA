# Write a function solve_for_x(equation: str) -> float that takes a string representing a linear equation in the form ax+b=c or ax-b=c, where a, b, and c are integers. The function should return the value of x as a float.

def solve_for_x(equation: str):
    equation = equation.strip()
    eqn =[]
    eqnstr =""
    for i in equation:
        if i!=" ":
            eqnstr+=i
    # print(eqnstr)
    eqn = equation.split("=")
    LHS = str(eqn[0])
    RHS = int(eqn[1])
    a = 0
    c=0

    if "+" in LHS or "-" in LHS:
        splitLHS = []
        if "+" in LHS:
            splitLHS=LHS.split("+")
            c = 0 - int(splitLHS[1])
        elif "-" in LHS[1:]:
            splitLHS = LHS.split("-")
            c = int(splitLHS[1])

        if len(splitLHS[0])>1:
                firstTerm = splitLHS[0]
                # print("Term1",firstTerm)
                if splitLHS[0] == "-x":
                    a = -1
                elif splitLHS[0] == "x":
                    a = 1
                else:
                    numberoffirstterm = firstTerm[0:len(firstTerm)-2]
                    if len(numberoffirstterm)==0:
                        a = 1
                    else:
                        a = int(numberoffirstterm)
                    # print(a)
        
    else:
        a = int(LHS[0:len(LHS)-1])

    
    
    
    x = (int(RHS)+c)/a 
    return x 

print(solve_for_x("2x +3= 11"))
print(solve_for_x("5x -2 = 13"))
print(solve_for_x("-3x + 10=1"))
print(solve_for_x("x + 2 = 5"))
print(solve_for_x("2x=6"))
    
