class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int sum = 0;	// 세 수를 더한 값을 저장하기 위한 변수
        
        // 서로 다른 3개의 수를 더해서 소수인지 판별
        for(int i = 0; i < nums.length-2; i++){
            for(int j = i+1; j < nums.length-1; j++){
                for(int k = j+1; k < nums.length; k++){
                    sum = nums[i] + nums[j] + nums[k];
                    if(isPrime(sum)) answer++;
                }
            }
        }
        return answer;
    }
    
    // 소수인지 판별
    public boolean isPrime(int sum){
            boolean flag = true;
            
            for(int i = 2; i < sum; i++){
                if(sum % i == 0) flag = false;  // 소수가 아니면
            }
            
            return flag;
    }
}
