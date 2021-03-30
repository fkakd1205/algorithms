import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = {};
        List<Integer> list = new ArrayList<Integer>();  //List를 사용해 ArrayList 생성
        
        //arr의 각 요소 중 divisor로 나누어 떨어지는 값을 lsit에 넣는다.
        for(int k : arr){
            if(k % divisor == 0)
                list.add(k);
        }
        
        //나누어 떨어지는 값이 존재하지 않는다면
        if(list.isEmpty())
            list.add(-1);
        
        answer = new int[list.size()];
        
        for(int i = 0; i < answer.length; i++)
            answer[i] = list.get(i);
        
        //배열 오름차순 정렬
        Arrays.sort(answer);
        
        return answer;
    }
}
