import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.ListIterator;
// import java.util.Scanner;

// BOJ 5397 [키로거]
public class Main {
    // 연결리스트 사용 => 시간초과
    // public static void main(String[] args) {
    //     Scanner sc = new Scanner(System.in);
    //     LinkedList<Character> list = new LinkedList<>();

    //     int N = sc.nextInt();
    //     for(int i = 0; i < N; i++) {
    //         list = new LinkedList<>();
    //         String str = sc.next();
    //         int cursor = 0;

    //         for(int j = 0; j < str.length(); j++) {
    //             char c = str.charAt(j);
    //             if(c == '<') {
    //                 if(cursor != 0) {
    //                     cursor--;
    //                 }
    //             }else if(c == '>') {
    //                 if(cursor != list.size()) {
    //                     cursor++;
    //                 }
    //             }else if(c == '-') {
    //                 if(cursor != 0) {
    //                     cursor--;
    //                     list.remove(cursor);
    //                 }
    //             }else {
    //                 list.add(cursor, c);
    //                 cursor++;
    //             }
    //         }
            
    //         for(char c : list) {
    //             System.out.print(c);
    //         }

    //         System.out.print("\n");
    //     }
    // }

    // ListIterator 사용
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            LinkedList<Character> list = new LinkedList<>();
            ListIterator<Character> iter = list.listIterator();
            String str = br.readLine();

            for (int j = 0; j < str.length(); j++) {
                char c = str.charAt(j);
                if (c == '<') {
                    if (iter.hasPrevious()) {
                        iter.previous();
                    }
                } else if (c == '>') {
                    if (iter.hasNext()) {
                        iter.next();
                    }
                } else if (c == '-') {
                    if (iter.hasPrevious()) {
                        iter.previous();
                        iter.remove();
                    }
                } else {
                    iter.add(c);
                }
            }

            for (Character c : list) {
                bw.write(c);
            }
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}
