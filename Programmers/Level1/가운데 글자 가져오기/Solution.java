//가운데 글자 가져오기
class Solution {
	
    public String solution(String s) {
        String answer = "";
        
        if(s.length() % 2 == 0)	//s의 길이가 짝수인 경우
            answer = s.substring(s.length()/2-1, s.length()/2+1);
        else	//s의 길이가 홀수인 경우
            answer = s.substring(s.length()/2, s.length()/2+1);
        
        return answer;
    }
}