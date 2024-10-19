package day2.피보나치수5_10870;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

//        String file = "hdm/src/day2/피보나치수5_10870/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int cal = 0;
        int cal2 = 1;
        int pre = 0;
        if (n == 0){
            System.out.println(0);
        } else if (n == 1){
            System.out.println(1);
        } else {
            for (int i = 2; i <=n; i++){
                pre = cal2; // n-1 번째 값을 pre에 넣어주기
                cal2 = cal + cal2; // n 번째 높은값 생성.
                cal = pre; // n-2번째값이 이제 n-1로 대체됨.
            }
            System.out.println(cal2);
        }
        /*
        피보나치 수는 0과 1로 시작함.
         */

    }
}
