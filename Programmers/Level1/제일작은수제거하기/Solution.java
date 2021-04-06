import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        List<Integer> list = new ArrayList<Integer>();  //List를 사용해 ArrayList 생성
        
        if(arr.length == 1) {   //arr의 길이가 1일 때
            answer = new int[1];
            answer[0] = -1; //빈 배열인 경우 -1을 채운다
        }else{
            for(int i = 0; i < arr.length; i++){
                list.add(arr[i]);
            }
            
            int min = 0;
            for(int i = 1; i < arr.length; i++){
                if(arr[min] > arr[i]){  //가장 작은 수를 min에 넣기
                    min = i;
                }
            }
            
            list.remove(min);   //가장 작은 수 제거
            answer = new int[list.size()];
            
            for(int i = 0; i < list.size(); i++){
                answer[i] = list.get(i);
            }
        }
        return answer;
    }
}
