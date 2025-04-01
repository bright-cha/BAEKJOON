import java.util.Scanner;

class Main {

    public static final int MAX_N = 116;

    public static long[] memo = new long[MAX_N + 1];
    public static int n;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();

        memo[1] = 1;
        memo[2] = 1;
        memo[3] = 1;

        System.out.println(solve(n));
    }

    public static long solve(int x) {
        if (memo[x] != 0)
            return memo[x];

        return memo[x] = solve(x - 1) + solve(x - 3);
    }
}