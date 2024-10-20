import java.io.*;
import java.util.StringTokenizer;

public class BOJ10818_최소최대 {
    public static void main(String args[]) throws IOException {
        // buffer로 입력받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());    // br: 각 줄 입력, st: 각 줄 입력받은 st를 공백기준으로 분리
        int n = Integer.parseInt(st.nextToken());   // n: 정수형으로 입력 받기

        int[] numArray = new int[n];    // 크기가 n인 정수형 배열 numArray 선언

        st = new StringTokenizer(br.readLine());    // 새로 한 줄 입력받기

        // numArray 배열에 입력받은 n개의 정수 저장
        for (int i=0;i<n;i++) {
            numArray[i] = Integer.parseInt(st.nextToken());
        }

        // 최소값과 최대값으로 이루어진 정수형 배열 선언 및 초기화
        int[] minMaxArray = {1000000, -1000000};

        // numArray(입력받은 n개의 정수)의 모든 요소에 대해 최대/최소값인지 확인하기
        for (int i=0;i<n;i++) {
            // 최대값 갱신
            if (numArray[i] > minMaxArray[1]) {
                minMaxArray[1] = numArray[i];
            }

            // 최소값 갱신
            if (numArray[i] < minMaxArray[0]) {
                minMaxArray[0] = numArray[i];
            }
        }

        // 정답출력
        for (int num:minMaxArray) {
            System.out.print(num + " ");
        }
    }
}
