class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        for(int i = 0; i < n; i++){
            answer[i] = Integer.toBinaryString(arr1[i] | arr2[i]); //비트연산, 하나라도 1이면 1 아니면 0
        }
        
        for(int i = 0; i < n; i++){
            //문자열 자릿수 지정(%n), 자릿수를 지정하지 않으면 문자열 첫번째에 공백이 들어왔을 때 출력 x
            answer[i] = String.format("%" + n + "s", answer[i]); 
            answer[i] = answer[i].replace("1", "#");
            answer[i] = answer[i].replace("0", " ");
        }
        
        return answer;
    }
}