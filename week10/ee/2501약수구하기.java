import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int cnt = 0;


        for (int i = 1; i <= p; i++) {
            if (p % i == 0) {
                cnt += 1;
            }
            if (cnt == q) {
                System.out.println(i);
                break;
            }
        }
        if (cnt < q) {
            System.out.println(0);
        }
    }
}