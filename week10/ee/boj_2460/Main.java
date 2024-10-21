package boj_2460;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int now = 0;
        int max = 0;

        for (int i = 0; i < 10; i++) {
            String s = br.readLine();
            StringTokenizer st = new StringTokenizer(s);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            now = now - a + b;
            if (now > max) {
                max = now;
            }
        }

        System.out.println(max);
    }
}
