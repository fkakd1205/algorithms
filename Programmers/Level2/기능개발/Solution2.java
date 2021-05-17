import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution2 {
	public int[] solution(int[] progresses, int[] speeds) {
		int[] answer = {};
		Stack<Integer> progress = new Stack<Integer>();
		List<Integer> complete = new ArrayList<Integer>();	// 완료된 작업의 개수를 저장
		int preLength = progresses.length;	// 남아있는 작업들의 개수
        int task = 0;	// 배포되지 않은 작업의 인덱스 저장
        
		for(int i = progresses.length-1; i >= 0; i--) {
			progress.push(progresses[i]);	// 마지막 작업부터 stack에 넣는다.
		}
		
        while(true) {
			for (int i = 0; i < progresses.length; i++) {
				progresses[i] += speeds[i];
			}
			
			// task번째 부터 progresses의 크기만큼
			for(int i = task; i < progresses.length; i++) {
				if(progresses[i] >= 100) {
					progress.pop();	//  작업도가 100이상일 때, 먼저 배포되어야하는 작업 pop
				}
				else {
					task = i;	// 배포되지 않은 작업의 인덱스
					break;
				}
			}
			
			// 완료된 작업이 있다면
			if(progress.size() != preLength)	{
				complete.add(preLength - progress.size());	// 완료된 작업의 개수 저장
				preLength = progress.size();	// 남아있는 작업들의 개수 변경
			}
			
			if(progress.isEmpty()) break;	// 모든 작업이 완료되었다면, 종료
        }
        
        answer = new int[complete.size()];
		for(int i = 0; i < answer.length; i++) {
			answer[i] = complete.get(i);
		}
        return answer;
    }
}
