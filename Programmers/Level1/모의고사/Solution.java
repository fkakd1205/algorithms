import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] person1 = {1, 2, 3, 4, 5};
        int[] person2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] person3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] ans = new int[3];
        
        for(int i = 0; i < answers.length; i++) {
        	if(answers[i] == person1[i % 5]) ans[0]++;
        	if(answers[i] == person2[i % 8]) ans[1]++;
        	if(answers[i] == person3[i % 10]) ans[2]++;
        }
        
        //가장 정답률이 높은 학생의 점수
        int max = Math.max(Math.max(ans[0], ans[1]), ans[2]);
        
        List<Integer> list = new ArrayList<Integer>();  //List를 사용해 ArrayList 생성
        
        if(max == ans[0]) list.add(1);
        if(max == ans[1]) list.add(2);
        if(max == ans[2]) list.add(3);
        
        answer = new int[list.size()];  //추가된 학생의 리스트 크기만큼 정답 배열의 크기를 지정
        
        //높은 점수를 받은 학생의 리스트를 정답 배열 answer에 저장
        for(int i = 0; i < answer.length; i++){
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}
