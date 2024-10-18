package day2.지능형기차_2460;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {

//        String file = "hdm/src/day2/지능형기차_2460/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<int[]> peopleList = new ArrayDeque<>();

        for (int i =0; i<10; i++){
            String input = br.readLine();
            String[] splitInput = input.split(" ");
            peopleList.add(new int[]{
                    Integer.parseInt(splitInput[0]),
                    Integer.parseInt(splitInput[1])
            });
        }

//        System.out.println(peopleList); //[[I@34a245ab, [I@7cc355be, [I@6e8cf4c6, [I@12edcd21, [I@34c45dca, [I@52cc8049, [I@5b6f7412, [I@27973e9b, [I@312b1dae, [I@7530d0a]

        int result = 0;
        int recentPeopleCnt = 0;

        for (int i =0; i<10; i++){
            int[] station = peopleList.pollFirst();
            recentPeopleCnt = recentPeopleCnt + station[1] - station[0];
            if (result < recentPeopleCnt){
                result = recentPeopleCnt;
            }
        }

        System.out.println(result);

        /*
        1번역 ~ 10번역까지 10개 정착역이 있는 노선에서 운행중.
        타거나 내리는 사람 수를 자동으로 인식하는 장치 있음.

        출발 ~ 종착역 과정중 기차 안 사람 가장 많을때 사람 수 계산.

         */
    }
}
