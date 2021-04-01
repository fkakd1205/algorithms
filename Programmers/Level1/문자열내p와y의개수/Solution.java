class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int pCnt = 0, yCnt = 0;
        char ch = ' ';
        
        for(int i = 0; i < s.length(); i++){
            ch = s.charAt(i);
            if(ch == 'p' || ch == 'P')
                pCnt++;
            else if(ch == 'y' || ch == 'Y')
                yCnt++;        
        }
        
        if(pCnt == yCnt) answer = true;
        else answer = false;

        return answer;
    }
}
