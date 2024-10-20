package day1.약수구하기_2501;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class 약수구하기 {
    public static void main(String[] args) throws IOException {

        String filePath = "hdm/src/day1/약수구하기_2501/input.txt";
        BufferedReader br = new BufferedReader(new FileReader(filePath));
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        String[] values = br.readLine().split(" ");
        int a = Integer.parseInt(values[0]), b = Integer.parseInt(values[1]);

        br.close();
        ArrayList<Integer> resultList = new ArrayList<>();

        for (int i = 1; i <= a; i++){
            if(a % i == 0){
                resultList.add(i);
            }
        }

        if (resultList.size() >= b){
            System.out.println(resultList.get(b-1));
        } else {
            System.out.println(0);
        }

//        System.out.println(resultList.get(b));

        /*
        values 0번째의 약수를 구한 후 1번째의 값을 출력하면됨.
         */

    }
}
