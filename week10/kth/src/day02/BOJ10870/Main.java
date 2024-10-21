package day02.BOJ10870;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long result = fibonacci(n);
        System.out.println(result);
    }

    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        }

        int prev = 0;
        int cur = 1;

        for (int i = 2; i <= n; i++) {
            int next = prev + cur;
            prev = cur;
            cur = next;
        }

        return cur;
    }
}