package day01.BOJ10818;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
//        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(reader.readLine());
        int[] numbers = Arrays.stream(reader.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int min = numbers[0];
        int max = numbers[0];

        for (int num: numbers) {
            if (num < min) {
                min = num;
            }

            if (num > max) {
                max = num;
            }
        }

        System.out.print(min + " ");
        System.out.print(max);
    }
}
