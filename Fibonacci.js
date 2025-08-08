// How it works:

// Start with the two first Fibonacci numbers 0 and 1.
// Add the two previous numbers together to create a new Fibonacci number.
// Update the value of the two previous numbers.
// Do point a and b above 18 times.

 // 0, 1, 1, 2, 3, 5, 8, 13, 21, ...


 let count = 0;
 let f = [0,1];

 for(let i = 0; i < 18;i++) {
    count = f[i] + f[i+1];
    f.push(count);
 }

 console.log(f);


let prev2 = 0
let prev1 = 1

console.log(prev2)
console.log(prev1)

for (let i = 1; i < 18; i++) {
    let newFibo = prev1 + prev2;
    console.log(newFibo);
    prev2 = prev1;
    prev1 = newFibo;
}

// pv2, pv1 = (0,1)
// nf (1 + 0) 
// nf = (1)
// pv2 = pv1 (pv2 = 1)
// pv1 = nf (pv1 = 1)

// pv2, pv1 = (1,1)
// nf (1 + 1)
// nf = (2)
// pv2 = pv1 (pv2 = 1)
// pv1 = nf (pv1 = 2)

// pv2, pv1 = (1,2)
// nf (2 + 1)
// nf = (3)
// pv2 = pv1 (pv2 = 2)
// pv1 = nf (pv1 = 3)

// Recursion
count = 2
console.log(0);
console.log(1);
function fibonacci(prev1, prev2) {
    if(count <= 19) {
        let newFibo = prev1 + prev2;
        console.log(newFibo);
        prev2 = prev1;
        prev1 = newFibo;
        count++;
        fibonacci(prev1, prev2);
    
    } else {
        return;
    }
}

fibonacci(1,0);

 





 

