import java.util.Stack;

public class Solution {
    static boolean solution(String s) {
        boolean answer = true;
        Stack<Character> st = new Stack<Character>();

        for(int i = 0; i < s.length(); i++) {
            // 스택이 비어있지 않고, s.charAt(i) 값이 ')'라면 스택에서 짝을 제거
            if(!st.isEmpty() && s.charAt(i) == ')'){
                st.pop();
            } else{     
                st.push(s.charAt(i));       // s.charAt(i) 값이 '('라면 스택에 넣기
            }
        }
        answer = st.isEmpty() ? true : false;       // 모두 짝지어졌다면 true, 그렇지 않다면 false
        return answer;
    }
}
