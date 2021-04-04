class Solution {
    public String solution(String s) {
        String answer = "";
        char c = ' ';
        int cnt = 0;
        
        for(int i = 0; i < s.length(); i++){
            c = s.charAt(i);
            if(c == ' '){	//s의 i번째 글자가 공백일 때
                cnt = 0;
            }
            else{
                if(cnt % 2 == 0){	//공백을 기준으로 인덱스가 짝수일때
                    c = Character.toUpperCase(c);	//대문자로 변경
                    cnt++;
                }else{	//공백을 기준으로 인덱스가 홀수일때
                    c = Character.toLowerCase(c);	//소문자로 변경
                    cnt++;
                }
            }
            answer += c;
        }
        return answer;
    }
}
