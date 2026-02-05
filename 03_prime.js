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

// My approach 2:
function myprime2(n){
    if(n<2){
        return 'neither prime nor composite'
    }
    // let status=true
    for (let i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
        if(n%i == 0){
            // status = false
            return false
        }
    }
    // return status
     return true
   

}

console.log(myprime2(1)); //neither nor
console.log(myprime2(20)); //false
console.log(myprime2(5)); //true

// bigO = O(root(n))
// Ins approach -- same