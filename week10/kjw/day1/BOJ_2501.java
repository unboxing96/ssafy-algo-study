package baekjoon;

import java.util.Scanner;

public class BOJ_2501 {
    public static void main(String[] args) {
//      스캐너로 입력 받아보기
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int count = 0;

        for (int i = 1; i <= N; i++) {
            if (N % i == 0) {
                count++;
                if (count == K) {
                    System.out.println(i);
                    return;
                }
            }
        }
        System.out.println(0);
    }
}
