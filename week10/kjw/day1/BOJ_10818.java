package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_10818 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] numbers = br.readLine().split(" ");

        int min_num = Integer.MAX_VALUE;
        int max_num = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(numbers[i]);
            if (num < min_num) {
                min_num = num;
            }

            if (num > max_num) {
                max_num = num;
            }
        }
        System.out.println(min_num + " " + max_num);

    }
}
