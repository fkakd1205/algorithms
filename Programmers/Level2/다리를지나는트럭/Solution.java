import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> bridge = new LinkedList<>();     // 다리 건너고있는 트럭들을 저장
        int sum = 0;    // 현재 다리를 건너고있는 트럭들의 무게 합
        
        for(int k : truck_weights){
            while(true){
                if(bridge.isEmpty()){   // 다리를 건너는 트럭이 없다면
                    bridge.add(k);
                    sum += k;
                    answer++;
                    break;
                }else if(bridge.size() == bridge_length){   // 다리를 건너는 트럭 개수가 다리의 길이와 동일한 경우
                    sum -= bridge.poll();   // 큐에서 가장 먼저 들어온 다리를 제거
                }else{
                    if(sum + k > weight){   // 다리를 건너는 트럭들의 무게 합과 다음 들어올 트럭의 무게의 합을 다리가 견디지 못한다면
                        bridge.add(0);  // 큐에 0을 넣는다.
                        answer++;
                    }else{
                        bridge.add(k);
                        sum += k;
                        answer++;
                        break;
                    }
                }
            }
        }
        // 마지막 트럭이 다리를 지나는 시간을 고려하지 않았으므로, 다리의 길이를 더해준다
        return answer + bridge_length;
    }
}
