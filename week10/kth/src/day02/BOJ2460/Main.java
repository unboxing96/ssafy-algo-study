package day02.BOJ2460;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int maxPeople = 0;
        int currentPeople = 0;

        for (int i = 0; i < 10; i++) {
            String[] input = br.readLine().split(" ");
            int getOff = Integer.parseInt(input[0]);
            int getOn = Integer.parseInt(input[1]);

            currentPeople -= getOff;
            currentPeople += getOn;

            if (currentPeople > maxPeople) {
                maxPeople = currentPeople;
            }
        }

        System.out.println(maxPeople);
    }
}