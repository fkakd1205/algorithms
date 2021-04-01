import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Set<Integer> set = new HashSet<>();  //Set을 사용하여 HashSet 생성, Set은 객체를 중복해서 저장할 수 없는 특징이 있다.
        
        for(int i = 0; i < nums.length; i++)
            set.add(nums[i]);
        
        //최대로 고를 수 있는 폰켓몬 종류 수
        if(set.size() < (nums.length/2))
            answer = set.size();
        else
            answer = nums.length/2;
        
        return answer;
    }
}
