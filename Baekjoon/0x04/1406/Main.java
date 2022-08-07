// import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.ListIterator;
// import java.util.Scanner;

// BOJ 1406 [에디터]
public class Main {
    
    // 연결리스트 사용 => 시간초과
    // public static void main(String[] args) {
    //     Scanner sc = new Scanner(System.in);
    //     LinkedList<Character> list = new LinkedList<>();
    //     int cursor = 0;

    //     String str = sc.next();
    //     for(int i = 0; i < str.length(); i++) {
    //         list.add(str.charAt(i));
    //         cursor++;
    //     }

    //     int op = sc.nextInt();
    //     for(int i = 0; i < op; i++) {
    //         String command = sc.next();
    //         if(command.equals("P")) {
    //             list.add(cursor++, sc.next().charAt(0));
    //         }else if(command.equals("B")) {
    //             if(cursor != 0) {
    //                 cursor--;
    //                 list.remove(cursor);
    //             }
    //         }else if(command.equals("L")) {
    //             if(cursor != 0) {
    //                 cursor--;
    //             }
    //         }else if(command.equals("D")) {
    //             if(cursor != list.size()) {
    //                 cursor++;
    //             }
    //         }
    //     }

    //     for(Character c : list) {
    //         System.out.print(c);
    //     }
    // }

    // ListIterator 사용 => 성공
    public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

            String str = br.readLine();
            int n = Integer.parseInt(br.readLine());

            LinkedList<Character> list = new LinkedList<>();

            for(int i = 0; i < str.length(); i++) {
                list.add(str.charAt(i));
            }

            ListIterator<Character> iter = list.listIterator();

            while(iter.hasNext()) {
                iter.next();
            }

            for(int i = 0; i < n; i++) {
                String command = br.readLine();
                char c = command.charAt(0);

                if(c == 'L') {
                    if(iter.hasPrevious()) {
                        iter.previous();
                    }
                }else if(c == 'D') {
                    if(iter.hasNext()) {
                        iter.next();
                    }
                }else if(c == 'B') {
                    if(iter.hasPrevious()) {
                        iter.previous();
                        iter.remove();
                    }
                }else if(c == 'P') {
                    char insertChar = command.charAt(2);
                    iter.add(insertChar);
                }
            }

            for(Character chr : list) {
                bw.write(chr);
            }

            bw.flush();
            bw.close();
        }
}
