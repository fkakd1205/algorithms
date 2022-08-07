import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int T = Integer.parseInt(reader.readLine());
        String number = "";
        int sum = 0;

        for(int i = 0; i < T; i++) {
            number = reader.readLine();
            String[] num = number.split(" ");
            int num1 = Integer.parseInt(num[0]);
            int num2 = Integer.parseInt(num[1]);

            sum = num1 + num2;
            writer.write(String.valueOf(sum) + "\n");
        }

        reader.close();
        writer.close();
    }
}
