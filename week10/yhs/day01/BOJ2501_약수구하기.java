import java.io.*;
import java.util.StringTokenizer;

class BOJ2501_약수구하기 {
    public static void main(String args[]) throws IOException {
        // buffer로 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();   // s : 한 줄 입력 받은 것
        StringTokenizer st = new StringTokenizer(s);    // st : 한 줄 입력받은 s를 공백을 기준으로 분리

        // 각 줄의 입력 형식 : "p q"와 같이 공백을 두고 두 정수가 주어짐
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        // 정답(K번째 작은 약수) 초기화: 없을 경우 0
        int answer = 0;
        // 1부터 p까지 모든 정수에 대해 약수인지 확인하기
        for (int i = 1; i <= p; i++) {

            if (p % i == 0) {       // 약수 찾을 때마다 q 1씩 감소
                q--;

                if (q == 0) {       // q가 0이 되면(q번째 약수까지 찾았다면)
                    answer = i;     // K번째 작은 약수 저장하고 반복 탈출!
                    break;
                }
            }
        }
        System.out.println(answer); // 정답 출력하기
    }
}