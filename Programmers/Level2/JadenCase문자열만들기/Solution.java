class Solution {
    public static String solution(String s) {
        String answer = "";
        StringBuilder sb = new StringBuilder(s.toLowerCase());      // 모두 소문자로 변경
        boolean isBlank = true;     // 공백 확인. 항상 첫번째 문자는 대문자이므로 true로 설정

        for(int i = 0; i < sb.length(); i++) {
            if(isBlank){
                sb.setCharAt(i, Character.toUpperCase(sb.charAt(i)));
            }
            isBlank = (sb.charAt(i) == ' ') ? true : false;
        }

        answer = sb.toString();
        return answer;
    }
}
