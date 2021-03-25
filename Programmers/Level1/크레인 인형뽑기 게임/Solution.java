import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> basket = new Stack<Integer>();
        
        for(int i = 0; i < moves.length; i++){
            for(int j = 0; j < board.length; j++){
                if(board[j][moves[i]-1] != 0){
                    //바구니가 비었는지 확인
                    if(basket.isEmpty())
                        basket.push(board[j][moves[i]-1]);
                    else{
                        //바구니에 연속적으로 동일한 인형이 들어왔는지 확인
                        if(basket.peek() == board[j][moves[i]-1]){
                            basket.pop();	//동일 인형 제거
                            answer += 2;
                        }
                        else
                            basket.push(board[j][moves[i]-1]);	//바구니에 인형 담기
                    }
                    
                    board[j][moves[i]-1] = 0;   //바구니에 옮겨 담았으므로 왼쪽게임에서 인형을 제거
                    break;
                }
            }
        }
        return answer;
    }
}
