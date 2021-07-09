class Solution {
    public String solution(String number, int k) {
        String answer = "";
        int idx = 0;
        char maxChar = '0';
        StringBuilder sb = new StringBuilder();

        // k개가 제거되므로 length()-k 까지 구한다
        for(int i = 0; i < number.length()-k; i++) {
            maxChar = '0';

            // 범위 내 가장 큰 수를 구한다
            for(int j = idx; j <= k+i; j++){
                if(maxChar < number.charAt(j)){
                    maxChar = number.charAt(j);
                    idx = j+1;
                }
            }
            sb.append(maxChar);
        }

        answer = sb.toString();
        return answer;
    }
}
