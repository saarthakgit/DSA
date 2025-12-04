// Given a number 'n' find the first n terms of the fibonacci sequence

// in fibonacci sequence, every term is the sum of preceding 2 terms, and the first two are: 0,1

// MY ATTEMPT:
console.log(myfibonacci(5))

function myfibonacci(n){
    let i = 1
const seq = [0,1]
while (seq.length<n) {
    let j = i-1
    seq.push(seq[i]+seq[j])
    i+=1
}
return seq;
}

// Instructor's approach : 
function fibonacci(n){
    const seq = [0,1]
    for (let i = 2; i < n; i++) {
        seq[i] = seq[i-1] + seq[i-2]
        
    }
    return seq;
    
}

console.log(fibonacci(5));

// BigO for my approach : 3n-3 ----> O(n) , linear
// BigO for ins. approach : n --- > O(n) , linear