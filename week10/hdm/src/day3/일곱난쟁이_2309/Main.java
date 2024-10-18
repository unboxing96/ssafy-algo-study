package day3.일곱난쟁이_2309;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {

    public static void findCombination(ArrayList<Integer> dwarfs, int start, int depth, List<Integer> current, List<List<Integer>> result){
        if (depth == 7){
            int sum = 0;
            for (int num : current){
                sum += num;
            }
            if (sum == 100){
                result.add(new ArrayList<>(current));
            }
            return;
        }

        for (int i = start; i < dwarfs.size(); i++){
            current.add(dwarfs.get(i)); // 현재 드워프의 i를 current에 저장한다음,
            findCombination(dwarfs, i+1, depth+1, current, result);
            current.remove(current.size()-1); // 마지막 원소 제거. sum이 100인것을 못찾아서 return 맞고온것.
        }
    }


    public static void main(String[] args) throws IOException {

//        String file = "hdm/src/day3/일곱난쟁이_2309/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> sevenDwarfs = new ArrayList<>();

        for (int i = 0; i < 9; i++){
            int input = Integer.parseInt(br.readLine());
            sevenDwarfs.add(input); // [20, 7, 23, 19, 10, 15, 25, 8, 13]
        }
//        System.out.println(sevenDwarfs);

        Collections.sort(sevenDwarfs); // [7, 8, 10, 13, 15, 19, 20, 23, 25]
        List<List<Integer>> result = new ArrayList<>();
        findCombination(sevenDwarfs, 0, 0, new ArrayList<>(), result);

        for (int j = 0; j < 7; j++){
            System.out.println(result.get(0).get(j));
        }



        /*
        난쟁이 7명 x 9명이 나타남.
        난쟁이의 키합은 100.
        아홉 난쟁이의 키가 주어졌을때, 일곱 난쟁이를 찾는 프로그램?

        정답이 여러가지인 경우 아무거나 출력.
        오름차순으로 출력.

         */

    }
}
