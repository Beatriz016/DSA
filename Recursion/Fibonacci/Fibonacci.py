# How it works:

# Start with the two first Fibonacci numbers 0 and 1.
# Add the two previous numbers together to create a new Fibonacci number.
# Update the value of the two previous numbers.
# Do point a and b above 18 times.

 # 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

# Loop 
prev2 = 0
prev1 = 1

print(prev2)
print(prev1)
for fibo in range(18):
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo


# Recursion
print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)


# Finding The nth Fibonacci Number Using Recursion

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(19)) # generate the 20th Fibonacci number


