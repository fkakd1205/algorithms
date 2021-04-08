class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int sum = 0;
        
        for(int i = 0; i < arr.length; i++)
            sum += arr[i];
        
        answer = (double)sum / arr.length;	// 구한 합을 arr의 길이로 나눠 평균을 구한다.
        
        return answer;
    }
}
