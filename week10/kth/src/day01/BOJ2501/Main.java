package day01.BOJ2501;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
//        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String[] lines = reader.readLine().split(" ");
        int n = Integer.parseInt(lines[0]);
        int k = Integer.parseInt(lines[1]);
        reader.close();

        List<Integer> k_array = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                k_array.add(i);
            }
        }

        if (k_array.size() >= k) {
            System.out.println(k_array.get(k - 1)); // k번째 약수 출력
        } else {
            System.out.println(0); // k번째 약수가 없을 경우 0 출력
        }
    }
}
