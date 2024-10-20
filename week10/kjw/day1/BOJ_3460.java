package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_3460 {
    public static void main(String[] args) throws IOException {
//        버퍼로 입력받는 법, 앞으로는 이렇게 쭉 진행할 것
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 1; i <= T; i++) {
            int n = Integer.parseInt(br.readLine());
            int idx = 0;

            while (n > 0) {
                if (n % 2 == 1) {
                    System.out.print(idx + " ");
                    idx++;
                    n = n / 2;
                } else {
                    idx++;
                    n = n / 2;
                }
            }
            System.out.println();

        }
    }
}
