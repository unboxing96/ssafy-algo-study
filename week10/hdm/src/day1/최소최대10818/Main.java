package day1.최소최대10818;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {

//        String file = "hdm/src/day1/최소최대10818/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
//
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String strInput = br.readLine();
        String [] inputList = strInput.split(" "); // [20, 10, 35, 30, 7]
//        System.out.println(inputList[0]);
        int minNumber = Integer.parseInt(inputList[0]);
        int maxNumber = minNumber;

        for (int i = 0; i < N; i++){
            if (maxNumber < Integer.parseInt(inputList[i])){
                maxNumber = Integer.parseInt(inputList[i]);
            }
            if (minNumber > Integer.parseInt(inputList[i])){
                minNumber = Integer.parseInt(inputList[i]);
            }
        }

        System.out.printf("%d %d", minNumber, maxNumber);
        /*
        N개의 정수가 주어지고 최솟값 최대값 구하는 프로그램
         */
    }
}
