class Solution {
    public String solution(String s, int n) {
        String answer = "";
        char c = ' ';
        
        for(int i = 0; i < s.length(); i++){
            c = s.charAt(i);
            if(c != ' '){
                if(Character.isLowerCase(c)){   //c가 소문자인 경우
                    c = (char)(c + (n % 26));   //어떤 수를 더하더라도 알파벳 출력 <- n%26
                    if(c > 'z') c -= 26;    //z 다음 문자로 a를 셋팅
                }
                else if(Character.isUpperCase(c)){  //c가 대문자인 경우
                    c = (char)(c + (n % 26));
                    if(c > 'Z') c -= 26;    //Z 다음 문자로 A를 셋팅
                }
            }
            answer += c;
        }
        return answer;
    }
}
