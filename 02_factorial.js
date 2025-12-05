// Given a number n, find the factorial of it

// My Approach
function myfactorial(n){
    let f = 1  //the factorial of 0,1
    if (n>1) {
        for (let i = n; i >= 2; i--) {
        f = f*i
        }
    return f
    } else {
        return f
    }
    
}

console.log(myfactorial(5));

// BigO = linear O(n)

// Ins Approach:
function factorial(n){
    f = 1
    for (let i = n; i >= 2; i--) {
            f = f*i
            }
            return f
}

console.log(factorial(5));

// BigO O(n) -- linear