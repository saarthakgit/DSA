# Write a recursive function called count_down(n) that prints numbers from n down to 1, and then prints "Blastoff!".
def count_down(n):
    print(n)
    if n==1:
        return ("Blastoff!")
    else:
        return count_down(n-1)

# print(count_down(5))

# Write a recursive function reverse_string(s) that takes a string s and returns it backwards.

def reverse_string(s):
    print("init by:",s)
    if len(s)==1:
        return s
        
    else:
        print(s[-1] + reverse_string(s[:-1]))
    return s

# print(reverse_string("sar")) 


#  Write a recursive function power(base, exponent) that calculates base raised to the power of exponent (e.g., $x^y$). Do not use Python's built-in ** operator or math.pow().

def power(base,expo):
    # means x*x for expo = 2, x*x*x for 3 and so on 
    if expo ==1:
        return base 
    else:
        return base*(power(base,expo-1))
    
# print(power(2,3)) 

# Write a recursive function is_palindrome(s) that takes a string and returns True if it is a palindrome (reads the same forwards and backwards) and False if it is not.

# without recursion
"""def is_palindrome(s):
    if s[::-1] == s:
        return True 
    else:
        return False"""
# with recursion:

def is_palindrome(s):
    # print("init with",s)
    if len(s)<=1:
        return True 
    else:
        if s[0] != s[-1]:
            return False 
        else:
            return is_palindrome(s[1:len(s)-1])

# print(is_palindrome("o"))

#We have a line of n bunnies. Every bunny has exactly 2 ears. Write a recursive function bunny_ears(n) that computes the total number of ears without using multiplication.

def bunny_ears(n):
    if n==0:
        return 0 
    else:
        return 2 + bunny_ears(n-1)
    
print(bunny_ears(4))
    
