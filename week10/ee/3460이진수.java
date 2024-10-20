import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();

        for (int tc = 0; tc < T; tc++) {

            int N = scanner.nextInt();
            int idx = 0;

            while (N > 0) {
                if (N % 2 == 1) {
                    System.out.print(idx + " ");
                }
                idx++;
                N /= 2;
            }
            System.out.println();
        }
    }
}