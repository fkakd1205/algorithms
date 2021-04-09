class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int len = phone_number.length();
        
        for(int i = 0; i < len; i++){
            if(i < len-4)	// 마지막 4개의 숫자를 제외하고 "*"로 변경
                answer += "*";
            else
                answer += phone_number.charAt(i);
        }
        
        return answer;
    }
}
