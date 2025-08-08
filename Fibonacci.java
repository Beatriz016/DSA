// How it works:

// Start with the two first Fibonacci numbers 0 and 1.
// Add the two previous numbers together to create a new Fibonacci number.
// Update the value of the two previous numbers.
// Do point a and b above 18 times.

 // 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

public class Main {
    public static void main(String[] args) {
        int prev2 = 0;
        int prev1 = 1;

        System.out.println(prev2);
        System.out.println(prev1);

        for(int fibo = 0; fibo < 18; fibo++) {
            int newFibo = prev1 + prev2;
            System.out.println(newFibo);
            prev2 = prev1;
            prev1 = newFibo;
        }
    }
}

// Recursion
public class Main {
    static int count = 2;

    public static void fibonacci(int prev1, int prev2) {
        if (count <= 19) {
            int newFibo = prev1 + prev2;
            System.out.println(newFibo);
            prev2 = prev1;
            prev1 = newFibo;
            count += 1;
            fibonacci(prev1, prev2);
        } else {
            return;
        }
    }

    public static void main(String[] args) {
        System.out.println(0);
        System.out.println(1);
        fibonacci(1, 0);
    }
}




