# Write a function excel_index that takes an Excel column name (e.g., "A", "Z", "AA", "AB", ..., "ZZZ") and returns its corresponding 1-based index. This function should correctly handle column names beyond "Z", following the Excel column numbering system.

# excel index logic:
ask = input()
pres = len(ask)-1
lasttoadd = ord(ask[-1])-64
power = 1
result = 0
for i in ask[-2::-1]:
    pos = ord(i)-64 
    prd = (26**(power))*pos 
    power+=1
    result+=prd 

result+=lasttoadd
print(result)