class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        char c = ' ';
        
		for(int i = 0; i < s.length(); i++) {
			c = s.charAt(i);
			
			//숫자가 아니라면 false
			if(c < '0' || c > '9') {
				answer = false;
                break;
			}
		}
        
        if(s.length() != 4 && s.length() != 6) answer = false;
        
        return answer;
    }
}
