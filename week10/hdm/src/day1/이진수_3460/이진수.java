package day1.이진수_3460;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

import java.util.Collections;


public class 이진수 {
    public static void main(String[] args) throws IOException {

//        String filePath = "hdm/src/day1/이진수_3460/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(filePath));
//
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++){
            int n = Integer.parseInt(br.readLine());
            ArrayList<Integer> positions = new ArrayList<>();
            int position = 0;

            while (n > 0){
                if (n % 2 == 1) {
                    positions.add(position);
                }
                n = n / 2;
                position++;
            }

            for (int i = 0; i < positions.size(); i++) {
                System.out.print(positions.get(i));
                if (i < positions.size() - 1) {
                    System.out.print(" ");
                }
            }

            System.out.println();

        }

        /*
        이진수로 나타냈을때, 1의 위치를 모두 찾는 프로그램. 최하위 비트의 위치는 0
        첫출에 테스트 케이스 T
        n이주어짐
         */
    }
}
