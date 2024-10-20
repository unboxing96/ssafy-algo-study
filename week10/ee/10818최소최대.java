
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();

//        int[] nums = new int[N];

        int minVal = Integer.MAX_VALUE;
        int maxVal = Integer.MIN_VALUE;

        for (int i = 0; i < N; i++) {
//            nums[i] = scanner.nextInt();
            int num = scanner.nextInt();
            if (num > maxVal) {
                maxVal = num;
            }
            if (num < minVal) {
                minVal = num;
            }
        }

        System.out.println(minVal + " " + maxVal);

    }
}