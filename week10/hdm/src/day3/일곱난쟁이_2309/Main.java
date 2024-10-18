package day3.일곱난쟁이_2309;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {

        String file = "hdm/src/day3/일곱난쟁이_2309/input.txt";
        BufferedReader br = new BufferedReader(new FileReader(file));

        ArrayList<Integer> sevenDwarfs = new ArrayList<>();

        for (int i = 0; i < 9; i++){
            int input = Integer.parseInt(br.readLine());
            sevenDwarfs.add(input); // [20, 7, 23, 19, 10, 15, 25, 8, 13]
        }
//        System.out.println(sevenDwarfs);

        Collections.sort(sevenDwarfs); // [7, 8, 10, 13, 15, 19, 20, 23, 25]






        /*
        난쟁이 7명 x 9명이 나타남.
        난쟁이의 키합은 100.
        아홉 난쟁이의 키가 주어졌을때, 일곱 난쟁이를 찾는 프로그램?

        정답이 여러가지인 경우 아무거나 출력.
        오름차순으로 출력.

         */

    }
}
