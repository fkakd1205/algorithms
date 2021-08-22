import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public String solution(String s) {
        String answer = "";
        List<Integer> number = new ArrayList<Integer>();
        String[] str = s.split(" ");

        for(int i = 0; i < str.length; i++){
            number.add(Integer.parseInt(str[i]));
        }

        // 오름차순 정렬
        Collections.sort(number);

        // 최소, 최대값 설정
        answer = number.get(0) + " " + number.get(number.size()-1);

        return answer;
    }
}