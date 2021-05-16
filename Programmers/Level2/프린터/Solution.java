import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
		
		// Integer형 PriorityQueue 우선순위 큐. 우선 순위가 높은 숫자 순으로 정렬 (내림차순 정렬)
		PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
		
		for(int k : priorities) {
			priorityQueue.add(k);
		}
		
		// 우선순위 큐가 비지 않을 때까지 돌면서 확인. location도 확인해야하므로.
		while(!priorityQueue.isEmpty()) {
			for (int i = 0; i < priorities.length; i++) {
				if (priorities[i] == priorityQueue.peek()) {	// 우선 순위가 높은 것부터 검사
					if (i == location)	return answer;	// 찾고 있는 수가 location에 위치한 숫자가 맞으면 리턴
					
					// 찾고 있는 수가 아니지만 숫자가 동일한 경우.
					priorityQueue.poll();
					answer++;
				}
			}
		}
		
	    return answer;
    }
}
