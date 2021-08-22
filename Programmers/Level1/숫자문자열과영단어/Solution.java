class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] num = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
        String[] word = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        
        for(int i = 0; i < num.length; i++){
            s = s.replace(word[i], num[i]);
        }
        answer = Integer.parseInt(s);
        return answer;
    }
}
