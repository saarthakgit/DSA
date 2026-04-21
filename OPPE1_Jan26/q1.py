n = input()

def checknum(n):
    if len(n)!=10:
        return 
    count = 0
    corrected = ''
    if "l" in n or "o" in n:
        for i in n:
            if i=="l":
                i = "1"
                count+=1
            elif i=="o":
                i = "0"
                count+=1 
            corrected+=i
        print(count)
        print(corrected)

    else:
        print("No mistakes")

checknum(n)

