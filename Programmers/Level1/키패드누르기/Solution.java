class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int leftHand = 10;  // 현재 left손 위치 * -> 10으로 바꿈.
        int rightHand = 12; // 현재 right손 위치 # -> 12로 바꿈.
        
        for(int num : numbers){
            if(num == 1 || num == 4 || num == 7){   // left손 담당이면
                answer += "L";
                leftHand = num;     // 손 위치 변경
            }
            else if(num == 3 || num == 6 || num == 9){  // right손 담당이면
                answer += "R";
                rightHand = num;
            }
            else{   // 2, 5, 8, 0이 입력되었을 경우
                if(num ==0) num += 11;  // 0이면 11로 바꿈.(거리 계산을 위해)
                
                // Math.abs(num-XHand)/3 - x좌표 거리, Math.abs(num-XHand) - y좌표 거리
                // if. num = 5(1, 1), leftHand = 4(1, 0), rightHand = 9(2, 2)라고 하면
                // leftDis = 0+1 = 1, rightDis = 1+1 = 2. left손이 더 가까운 손을 알 수 있음.
				int leftDis = (Math.abs(num - leftHand))/3 + (Math.abs(num - leftHand))%3;
				int rightDis = (Math.abs(rightHand - num))/3 + (Math.abs(rightHand - num))%3;
                
                if(leftDis < rightDis){    // left손과 더 가깝다면
                    answer += "L";
                    leftHand = num;
                }
                else if(leftDis > rightDis){    // right손과 더 가깝다면
                    answer += "R";
                    rightHand = num;
                }else{  // 거리 같다면
                    if(hand.equals("left")){    // 왼손잡이는 왼손 사용
                        answer += "L";
                        leftHand = num;
                    }else{     // 오른손잡이는 오른손 사용
                        answer += "R";
                        rightHand = num;
                    }
                }
            }
        }
        return answer;
    }
}
