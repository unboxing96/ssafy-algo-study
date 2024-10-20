//package day01.BOJ3460;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
//        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(reader.readLine());

        for (int tc = 0; tc < testCase; tc++) {
            int decimalNum = Integer.parseInt(reader.readLine());
            List<Integer> binaryNumArray = new ArrayList<>();

            // 이진수로 변환하기 -> 2로 계속 나눈다. 매번 나머지를 저장한다. 이진수
            int index = 0;
            while (decimalNum > 0) {
                if ((decimalNum % 2) == 1) {
                    binaryNumArray.add(index);  // 현재 위치에 1이 있다면 저장
                }
                decimalNum /= 2;
                index++;
            }

            for (int i = 0; i < binaryNumArray.size(); i++) {
                if (i == binaryNumArray.size() - 1) {
                    System.out.print(binaryNumArray.get(i));
                } else {
                    System.out.print(binaryNumArray.get(i) + " ");
                }
            }
            System.out.println();
        }
    }
}
