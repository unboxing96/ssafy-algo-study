import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ3460_이진수 {
    public static void main(String[] args) throws IOException {
        // buffer로 입력 받기(st: 한 줄 입력 받은 것)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // T: tc 개수 / 정수형으로 입력받기
        int T = Integer.parseInt(st.nextToken());

        // T번의 테스트케이스마다 실행
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());

            // n <= 1e6  ->  이진수로 약 2^20이므로 크기가 20인 배열 선언
            int[] binaryArray = new int[20];

            // 이진수로 변환하기
            for (int j = 19; j >= 0; j--) {
                if ((int) (n / Math.pow(2, j)) == 1) {
                    binaryArray[j] = 1;
                    n -= (int) Math.pow(2, j);

                } else {
                    binaryArray[j] = 0;
                }

            }

            // 정답 출력
            for (int j = 0; j < 20; j ++) {
                if (binaryArray[j] == 1) {
                    System.out.print(j + " ");
                }
            }
        }
    }
}
