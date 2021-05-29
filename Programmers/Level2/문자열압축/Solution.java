class Solution {
    public int solution(String s) {
        int answer = s.length();
        if(answer == 1) return 1;   // s의 길이가 1일 경우 압축 x.
        
        // 문자열이 잘라지는 개수
        // 잘라지는 문자열의 길이가 s길이의 절반보다 크면 압축할 필요가 없기때문에 s.length()/2까지만
        for(int k = 1; k <= s.length()/2; k++){
            StringBuilder saveStr = new StringBuilder();    // k개 단위로 압축되는 문자열을 저장
            
            for(int i = 0; i < s.length(); i = i+k){
                String word = "";   // 잘라진 문자열 저장
                
                // k개 단위로 자른 문자열을 저장
                if(i+k >= s.length()) word = s.substring(i, s.length());
                else word = s.substring(i, i+k);
                
                int cnt = 1;    // 문자열 중복 개수
                StringBuilder sb = new StringBuilder();
                
                for(int j = i+k; j < s.length(); j = j+k){
                    String word2 = "";  // 잘라진 문자열 뒷부분을 또 k개로 잘라서 저장
                    
                    // k개 단위로 자른 문자열을 저장
                    if(j+k >= s.length()) word2 = s.substring(j, s.length());
                    else word2 = s.substring(j, j+k);
                    
                    // 잘라진 문자열과 중복된다면
                    if(word.equals(word2)){
                        cnt++;
                        i = j;
                    }else{
                        break;
                    }
                }
                
                // 잘라진 문자열 연결. 중복되지 않으면 숫자쓰지 않고 바로 문자열 작성.
                if(cnt == 1) sb.append(word);
                else sb.append(cnt).append(word);
                
                // 최종 문자열
                saveStr.append(sb.toString());
            }
            
            // 가장 짧게 압축된 문자열을 answer로 지정하기
            answer = Math.min(answer, saveStr.toString().length());
        }
        return answer;
    }
}
