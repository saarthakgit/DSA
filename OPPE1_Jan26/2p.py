nn = input()
index = 0
for i in nn:
    if index%2==0 and not i.isalpha():
        print(" False") 
        break
    elif index%2!=0 and not i.isnumeric():
        print("False")
        break
    else:
        print("TRUE")
        break