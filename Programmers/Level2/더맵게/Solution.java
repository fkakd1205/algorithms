import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;

        // 우선 순위가 낮은 숫자 순으로 정렬된 큐
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        
        for(int scovVal : scoville) {
            priorityQueue.offer(scovVal);
        }

        while(priorityQueue.peek() < K) {
            if(priorityQueue.size() == 1) return -1;

            // 가장 맵지 않은 음식의 스코빌 지수, 두 번쨰로 맵지 않음 음식의 스코빌 지수 추출
            int min1 = priorityQueue.poll();
            int min2 = priorityQueue.poll();

            int sum = min1 + (min2 * 2);
            priorityQueue.offer(sum);
            answer++;
        }

        return answer;
    }
}