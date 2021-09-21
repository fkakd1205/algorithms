import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;

        // 오름차순 정렬
        Arrays.sort(people);

        int start = 0;
        int end = people.length-1;
        
        // 가장 작은 값과 큰 값을 더했을 때, limit값보다 작거나 같으면 구명보트 개수++
        // limit값보다 크다면 구명보트 개수++, 가장 작은 값과 두번째 큰 값을 더해 비교.
        while(start <= end) {
            if(people[start] + people[end] <= limit) {
                start++;
            }
            end--;
            answer++;
        }
        
        return answer;
    }
}
