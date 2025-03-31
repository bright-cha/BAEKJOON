import java.util.Scanner;

class Main {

    public static boolean[] isCheck;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        int n = sc.nextInt();

        isCheck = new boolean[n + 1];

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (isCheck[i]) continue;
            for (int j = i * i; j <= n; j += i) {
                isCheck[j] = true;
            }
        }

        for (int i = m; i <= n; i++) {
            if (1 < i && !isCheck[i]) System.out.println(i);
        }
    }
}