import java.util.List;
import java.util.ArrayList;

public class Solution {
	public static int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        List<Integer> complete = new ArrayList<Integer>(); // 완료된 작업의 개수를 저장
        int count = 0;	// 완료된 작업을 카운트
        int task = 0;	// 배포되지 않은 작업의 인덱스
        boolean end = false;	// 마지막 작업의 완료 여부
        
        while(true) {
			for (int i = 0; i < progresses.length; i++) {
				progresses[i] += speeds[i];
			}
			
			for(int i = task; i < progresses.length; i++) {
				if(progresses[i] >= 100) {
					count++;
					if(i == progresses.length-1) end = true;	// 마지막 작업이 완료되었다면 end로 체크
				}
				else {
					task = i;	// 배포되지 않은 작업의 인덱스
					break;
				}
			}
			
			// 완료된 작업이 있다면
			if(count != 0)	{
				complete.add(count);	// 완료된 작업의 개수 저장
				count = 0;	// 완료 작업 개수 초기화
			}
			
			// 모든 작업이 완료되면
			if(end) break;
        }
        
        answer = new int[complete.size()];
		for(int i = 0; i < answer.length; i++) {
			answer[i] = complete.get(i);
		}
        return answer;
    }

}
