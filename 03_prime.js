// Given a number n, find if it is prime or not

// My approach : checking if we get a factor from 1 to half of that number, except 1
function myprime(n){
    let count = 0    // 0 factors apart from 1 and itself
    for (let i = 2; i <= (n/2); i++) {   
        if (n%i == 0) {
            count+=1
        }
    }
    if (count>0) {
        return false;
    } else {
        return true
    }
}

// console.log(myprime(2)); //true
// console.log(myprime(3)); //true
// console.log(myprime(4)); //false
// console.log(myprime(5)); //true
// console.log(myprime(9)); //false


// Ins approach --